# -*- coding: utf-8 -*-
"""Переносит внешние (хотлинк) картинки глав географии внутрь репозитория.

Свободные по лицензии изображения (Commons, USGS, NASA, NWS, ICS, журналы CC BY и др.),
скачанные браузером, кладутся в geography/assets/imported/, ссылки в md заменяются на локальные.
Изображения с неподтверждённой или неподходящей лицензией (CC BY-NC-SA, неизвестная, «все права защищены»)
вместе с подписью убираются из текста.
Запуск: python3 tools/geo-maps/localize.py [--dry]
"""
import re, glob, json, os, sys, urllib.parse
from PIL import Image

ROOT = '/home/claude/atlas-of-knowledge/geography/'
SRC = '/mnt/user-data/uploads/Downloads/'
OUT = ROOT + 'assets/imported/'
DRY = '--dry' in sys.argv

REMOVE_HOSTS = ('atlasofmaps.com', 'openstax.org', 'cdn.serc.carleton.edu', 'files.isric.org')

EXTRA = {
    'relief_map_of_europe.jpg': ('atlas_bga_europe.jpg', 'bga-relief-europe'),
    'relief_map_of_north_america.jpg': ('atlas_bga_north_america.jpg', 'bga-relief-north-america'),
    'relief_map_of_south_america.jpg': ('atlas_bga_south_america.jpg', 'bga-relief-south-america'),
    'relief_map_of_oceania.jpg': ('atlas_bga_oceania.jpg', 'bga-relief-oceania'),
    'relief_map_of_kyrgyzstan.jpg': ('atlas_bga_kyrgyzstan.jpg', 'bga-relief-kyrgyzstan'),
    'blank-map-of-kyrgyzstan-borders.svg': ('atlas_bm_borders.svg', 'ocha-kyrgyzstan-borders'),
    'blank-map-of-kyrgyzstan-labels.svg': ('atlas_bm_labels.svg', 'ocha-kyrgyzstan-labels'),
    '41597_2025_4892_Fig10_HTML.png': ('atlas_springer_fig10.png', 'sdata-human-modification'),
}

NONWM = json.load(open('/tmp/nonwm.json'))  # порядок = индексы atlas_ext_N
WM = json.load(open(SRC + 'atlas_wm_meta.json', encoding='utf-8'))
WMK = list(WM.keys())  # порядок = индексы atlas_wm_N


def wm_name(u):
    p = urllib.parse.urlparse(u).path
    if '/commons/thumb/' in p:
        n = p.split('/commons/thumb/')[1].split('/')[2]
    elif 'FilePath/' in p:
        n = p.split('FilePath/')[1]
    else:
        n = p.split('/')[-1]
    return urllib.parse.unquote(n).replace('_', ' ')


def src_for(u):
    """Вернёт (путь к скачанному файлу, лицензия/автор или None, slug) либо None."""
    if 'wikimedia.org' in u:
        k = wm_name(u)
        if k not in WM:
            return None
        i = WMK.index(k)
        for e in ('png', 'jpg', 'svg', 'gif'):
            f = f'{SRC}atlas_wm_{i}.{e}'
            if os.path.exists(f):
                return f, WM[k], 'wm-' + re.sub(r'[^a-z0-9]+', '-', os.path.splitext(k)[0].lower()).strip('-')[:48]
        return None
    b = u.split('?')[0].rsplit('/', 1)[-1]
    if b in EXTRA:
        return SRC + EXTRA[b][0], None, EXTRA[b][1]
    if u in NONWM:
        i = NONWM.index(u)
        for e in ('png', 'jpg', 'gif', 'webp'):
            f = f'{SRC}atlas_ext_{i}.{e}'
            if os.path.exists(f):
                stem = re.sub(r'[^a-z0-9]+', '-', os.path.splitext(u.split('?')[0].rsplit('/', 1)[-1])[0].lower()).strip('-')[:48]
                return f, None, 'ext-' + stem
    return None


def convert(f, slug):
    ext = os.path.splitext(f)[1].lower()
    if ext == '.svg':
        dst = OUT + slug + '.svg'
        if not DRY:
            open(dst, 'wb').write(open(f, 'rb').read())
        return os.path.basename(dst)
    im = Image.open(f)
    big = 2600 if 'chronostrat' in slug else 1600
    if im.width > big:
        im = im.resize((big, round(im.height * big / im.width)), Image.LANCZOS)
    if ext == '.gif':
        dst = OUT + slug + '.png'; im.convert('RGB').save(dst, optimize=True) if not DRY else None
        return os.path.basename(dst)
    rgb = im.convert('RGB') if im.mode not in ('RGB',) else im
    keep_png = ext in ('.png', '.webp') and not (ext == '.png' and os.path.getsize(f) > 1_500_000)
    if keep_png:
        dst = OUT + slug + '.png'
        if not DRY:
            im.save(dst, optimize=True)
            if os.path.getsize(dst) > 1_200_000:
                dst = OUT + slug + '.jpg'; os.remove(OUT + slug + '.png'); rgb.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    else:
        dst = OUT + slug + '.jpg'
        if not DRY:
            rgb.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    return os.path.basename(dst)


def main():
    os.makedirs(OUT, exist_ok=True)
    done = {}
    removed = []
    missing = []
    IMG = re.compile(r'^!\[[^\]]*\]\((https?://[^)\s]+)\)\s*$')
    for p in sorted(glob.glob(ROOT + 'chapters/*.md')):
        L = open(p, encoding='utf-8').read().split('\n')
        out = []
        i = 0
        while i < len(L):
            l = L[i]
            m = IMG.match(l)
            if not m:
                # встроенная ссылка в строке с другим текстом — не трогаем, но сообщим
                if re.search(r'!\[[^\]]*\]\(https?://', l):
                    out.append(l); missing.append((os.path.basename(p), 'inline', l[:80]))
                else:
                    out.append(l)
                i += 1; continue
            u = m.group(1)
            if any(h in u for h in REMOVE_HOSTS):
                # убрать подпись-метку выше (**Иллюстрация…) и подпись ниже (*…*)
                while out and out[-1].strip() == '':
                    out.pop()
                lab = None
                if out and re.match(r'^\*\*(Иллюстрация|Illustration|Figure|Рис)', out[-1].strip()):
                    lab = out.pop()
                removed.append((os.path.basename(p), u.rsplit('/', 1)[-1][:40], (lab or '')[:70]))
                i += 1
                # пропустить пустые и следующую строку-подпись
                j = i
                while j < len(L) and L[j].strip() == '':
                    j += 1
                if j < len(L) and L[j].startswith('*') and not L[j].startswith('**'):
                    i = j + 1
                continue
            s = src_for(u)
            if not s:
                missing.append((os.path.basename(p), 'nofile', u[:90])); out.append(l); i += 1; continue
            f, meta, slug = s
            if u not in done:
                done[u] = convert(f, slug)
            out.append(l.replace(u, '../assets/imported/' + done[u]))
            i += 1
        if not DRY:
            open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print('локализовано:', len(done), 'убрано:', len(removed))
    for r in removed:
        print('  УБРАНО', r)
    for m_ in missing:
        print('  ВНИМАНИЕ', m_)
    json.dump({u: v for u, v in done.items()}, open('/tmp/localized.json', 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
