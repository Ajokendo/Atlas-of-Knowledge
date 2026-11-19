# -*- coding: utf-8 -*-
"""Фото для глав географии: сжатие, подписи, вставка в md, запись в IMAGE_SOURCES.md.

Исходники: файлы atlas_<slot>.jpg и atlas_meta.json (метаданные Commons API),
которые браузер скачал в Downloads/Atlas PICS и которые подготовлены (staged) в песочницу.
Запуск:  python3 tools/geo-maps/photos.py <папка_с_файлами> [--sheet]
Идемпотентно: повторный запуск не дублирует вставки и записи.
"""
import json, glob, os, re, sys
from PIL import Image

ROOT = '/home/claude/atlas-of-knowledge/geography/'
CH = ROOT + 'chapters/'
OUT = ROOT + 'assets/photos/'
SRC = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads/Downloads/Atlas PICS'

# slot, имя файла, глава, начало заголовка, подпись RU, подпись EN
D = [
 # ---- Кыргызстан
 ('17-pass','too-ashuu-pass','17','## 17.3. ','Панорама перевала Тоо-Ашуу в Кыргызском Ала-Тоо. Через такие перевалы проходят главные дороги страны.','Panorama of the Too-Ashuu Pass in the Kyrgyz Ala-Too. The country’s main roads cross the mountains by passes like this one.'),
 ('17-tash','tash-rabat','17','## 17.11. ','Караван-сарай Таш-Рабат в горной долине Нарынской области — памятник Великого шёлкового пути.','The Tash Rabat caravanserai in a mountain valley of Naryn Region, a Silk Road monument.'),
 ('18-pobeda','pobeda-peak','18','### 18.5.1. ','Пик Жеңиш (Победы) над ледником Южный Иныльчек.','Jengish Chokusu (Victory Peak) above the South Inylchek Glacier.'),
 ('18-khan','khan-tengri','18','### 18.5.2. ','Хан-Тенгри на закате, вид с базового лагеря Южный Иныльчек.','Khan Tengri at sunset, seen from the South Inylchek base camp.'),
 ('18-lenin','lenin-peak','18','### 18.5.3. ','Пик Ленина, вид со стороны села Сары-Могол в Алайской долине.','Lenin Peak seen from the village of Sary-Mogol in the Alay Valley.'),
 ('18-inylchek','inylchek-valley','18','## 18.8. ','Ледниковая долина Комсомолец (съёмка с вертолёта над ледником Южный Иныльчек), Тянь-Шань.','The Komsomolets glacier valley (photographed from a helicopter over the South Inylchek Glacier), Tien Shan.'),
 ('19-chatyr','chatyr-kul','19','## 19.3. ','Озеро Чатыр-Куль на высокогорном плато Внутреннего Тянь-Шаня: здесь холодно даже летом.','Lake Chatyr-Kul on the high plateau of the Inner Tien Shan: it is cold here even in summer.'),
 ('19-skazka','skazka-canyon','19','## 19.4. ','Каньон Сказка на южном берегу Иссык-Куля: сухие глинистые склоны без леса.','Skazka Canyon on the southern shore of Issyk-Kul: dry clay slopes without forest.'),
 ('20-naryn','naryn-river','20','### 20.4.3. ','Река Нарын.','The Naryn River.'),
 ('20-boom','boom-gorge-chu','20','### 20.4.5. ','Река Чу у выхода из Боомского ущелья в Чуйскую долину.','The Chu River where it leaves the Boom Gorge and enters the Chuy Valley.'),
 ('20-talas','talas-river','20','### 20.4.6. ','Река Талас (участок у города Тараз, Казахстан).','The Talas River (near the city of Taraz, Kazakhstan).'),
 ('20-issyk','issyk-kul','20','### 20.6.1. ','Озеро Иссык-Куль и горы Тянь-Шаня.','Lake Issyk-Kul and the Tien Shan mountains.'),
 ('20-sonkul','song-kul-yurts','20','### 20.6.2. ','Юртовый лагерь у озера Сон-Куль: летние пастбища (джайлоо) на высоте более 3000 м.','A yurt camp by Lake Song-Kul: summer pastures (jailoo) above 3,000 m.'),
 ('20-sarychelek','sary-chelek','20','### 20.6.4. ','Озеро Сары-Челек.','Lake Sary-Chelek.'),
 ('20-merz','merzbacher-iss','20','### 20.6.5. ','Район озера Мерцбахера на леднике Иныльчек, снимок с Международной космической станции.','The area of Lake Merzbacher on the Inylchek Glacier, photographed from the International Space Station.'),
 ('20-toktogul','toktogul-reservoir','20','### 20.8.1. ','Токтогульское водохранилище.','The Toktogul Reservoir.'),
 ('20-kelsuu','kel-suu','20','## 20.6. ','Высокогорное озеро Кёль-Суу в Нарынской области.','High-mountain lake Kel-Suu in Naryn Region.'),
 ('21-edelweiss','edelweiss','21','## 21.3. ','Эдельвейс (Leontopodium ochroleucum) на перевале Барскоон, 3800 м, Терскей Ала-Тоо.','Edelweiss (Leontopodium ochroleucum) on the Barskoon Pass, 3,800 m, Terskey Ala-Too.'),
 ('21-walnut','arslanbob-walnut','21','## 21.4. ','Ореховый лес Арсланбоба в Джалал-Абадской области — один из крупнейших естественных ореховых лесов мира.','The Arslanbob walnut forest in Jalal-Abad Region, one of the largest natural walnut forests in the world.'),
 ('21-ibex','siberian-ibex','21','## 21.7. ','Сибирский горный козёл (Capra sibirica), снимок сделан в Кыргызстане.','Siberian ibex (Capra sibirica), photographed in Kyrgyzstan.'),
 ('21-argali','argali','21','## 21.7. ','Архар (Ovis ammon). Снимок сделан в Монголии (подвид Ovis ammon darwini); в Кыргызстане живёт другой подвид — тянь-шаньский архар.','Argali (Ovis ammon). Photographed in Mongolia (subspecies Ovis ammon darwini); Kyrgyzstan has a different subspecies, the Tien Shan argali.'),
 ('21-barys','snow-leopard','21','## 21.8. ','Снежный барс (ирбис). Фото сделано в зоопарке Ахтяри, Финляндия: в дикой природе зверя снимают редко.','Snow leopard. Photographed in Ähtäri Zoo, Finland: the animal is rarely photographed in the wild.'),
 ('22-sarychelek2','sary-chelek-reserve','22','## 22.4. ','Заповедник Сары-Челек: озеро в окружении горных лесов.','Sary-Chelek Reserve: a lake surrounded by mountain forests.'),
 ('22-alaarcha','ala-archa','22','## 22.5. ','Национальный парк «Ала-Арча» у Бишкека, вид сверху.','Ala-Archa National Park near Bishkek, seen from above.'),
 ('22-chonkemin','chon-kemin','22','## 22.5. ','Долина Чон-Кемин.','The Chon-Kemin Valley.'),
 ('23-yurt','yurt','23','## 23.10. ','Юрта в долине Чон-Кемин: традиционное жильё кочевников.','A yurt in the Chon-Kemin Valley, the traditional home of nomadic herders.'),
 ('24-burana','burana-tower','24','## 24.3. ','Башня Бурана — остаток города Баласагын, Чуйская область.','The Burana Tower, a remnant of the city of Balasagun, Chuy Region.'),
 ('24-karakol','karakol-church','24','## 24.5. ','Свято-Троицкий собор в Караколе, Иссык-Кульская область.','The Holy Trinity Cathedral in Karakol, Issyk-Kul Region.'),
 ('24-naryn','naryn-city','24','## 24.6. ','Вид на город Нарын.','View of the city of Naryn.'),
 ('24-walnut','arslanbob-walnut','24','## 24.7. ','Ореховые леса Арсланбоба в Джалал-Абадской области.','The Arslanbob walnut forests in Jalal-Abad Region.'),
 ('24-osh','sulaiman-too','24','## 24.8. ','Гора Сулайман-Тоо в Оше.','Sulaiman-Too mountain in Osh.'),
 ('24-batken','batken-mountains','24','## 24.9. ','Горы Баткенской области.','Mountains of Batken Region.'),
 ('25-bishkek','ala-too-square','25','## 25.3. ','Площадь Ала-Тоо в Бишкеке.','Ala-Too Square in Bishkek.'),
 ('25-hpp','akbulun-hpp','25','## 25.6. ','Ущелье Нарына в створе Акбулунской ГЭС: в таких ущельях строят плотины.','The Naryn gorge at the Akbulun hydropower site: dams are built in gorges like this.'),
 ('25-kumtor','kumtor','25','## 25.7. ','Золотой рудник Кумтор.','The Kumtor gold mine.'),
 ('26-kumtordump','kumtor-dump','26','## 26.9. ','Отвалы пустой породы на руднике Кумтор: добыча меняет рельеф и требует рекультивации.','Waste-rock dumps at the Kumtor mine: mining changes the landscape and requires reclamation.'),
 # ---- мир
 ('01-bluemarble','blue-marble','01','## 1.1. ','Земля из космоса. Составное изображение NASA «Голубой шарик» (Blue Marble) из данных спутников, а не один снимок.','Earth from space. NASA’s “Blue Marble” composite built from satellite data rather than a single photograph.'),
 ('02-aurora','aurora','02','## 2.3. ','Полярное сияние над Абиско (Швеция): свечение верхних слоёв атмосферы под действием солнечного ветра.','Aurora above Abisko (Sweden): glow of the upper atmosphere excited by the solar wind.'),
 ('03-basalt','basalt-columns','03','## 3.3. ','Базальтовые колонны «Дороги великанов» (Северная Ирландия): остывая, лава растрескивается на столбы.','Basalt columns of the Giant’s Causeway (Northern Ireland): cooling lava cracks into pillars.'),
 ('03-sanandreas','san-andreas','03','## 3.5. ','Разлом Сан-Андреас на плато Каррисо (Калифорния), вид из самолёта: прямая борозда внизу кадра. Здесь сдвигаются Тихоокеанская и Североамериканская плиты.','The San Andreas Fault on the Carrizo Plain (California) seen from an aircraft: the straight furrow at the bottom of the frame. The Pacific and North American plates slide past each other here.'),
 ('03-etna','etna-iss','03','## 3.7. ','Извержение Этны, снимок с Международной космической станции.','An eruption of Etna photographed from the International Space Station.'),
 ('03-folds','folds-hartland','03','## 3.8. ','Складки слоистых пород на мысе Хартленд-Пойнт (Англия).','Folded layered rocks at Hartland Point (England).'),
 ('04-canyon','grand-canyon','04','## 4.6. ','Большой каньон реки Колорадо: за миллионы лет река врезалась в плато более чем на 1,6 км.','The Grand Canyon of the Colorado River: over millions of years the river cut more than 1.6 km into the plateau.'),
 ('04-delta','lena-delta','04','## 4.6. ','Дельта Лены на снимке Landsat (в условных цветах).','The Lena Delta in a Landsat image (false colour).'),
 ('04-ushape','u-valley-glencoe','04','## 4.7. ','Троговая долина Глен-Ко (Шотландия), выработанная ледником.','The glacial trough Glen Coe (Scotland) carved by a glacier.'),
 ('04-dunes','sossusvlei','04','## 4.8. ','Дюны пустыни Намиб у Соссусфлей.','Dunes of the Namib Desert at Sossusvlei.'),
 ('04-fjord','geirangerfjord','04','## 4.10. ','Гейрангер-фьорд (Норвегия): ледниковая долина, затопленная морем.','Geirangerfjord (Norway): a glacial valley flooded by the sea.'),
 ('05-cb','cumulonimbus','05','## 5.7. ','Кучево-дождевое облако с «наковальней»: оно даёт ливни и грозы.','A cumulonimbus cloud with an anvil top, the source of downpours and thunderstorms.'),
 ('05-hurricane','hurricane-isabel','05','## 5.14. ','Ураган Изабель, вид с МКС: хорошо видны глаз и стена облаков.','Hurricane Isabel seen from the ISS: the eye and the eyewall are clearly visible.'),
 ('05-tornado','tornado','05','## 5.14. ','Грозовая суперячейка (США): из таких облаков выходят смерчи.','A supercell thunderstorm (USA): tornadoes descend from clouds like this.'),
 ('06-waves','waves','06','## 6.6. ','Прибойные волны у побережья Франции.','Breaking waves on the coast of France.'),
 ('06-reef','coral-reef','06','## 6.9. ','Коралловый риф на Большом Барьерном рифе (Австралия): один из самых продуктивных морских биомов.','A coral reef on the Great Barrier Reef (Australia), one of the most productive marine biomes.'),
 ('06-iceberg','iceberg','06','## 6.12. ','Айсберг в проливе Мак-Мердо (Антарктида), снимок NASA.','An iceberg in McMurdo Sound (Antarctica), a NASA photograph.'),
 ('06-amazon','amazon','06','## 6.13. ','Меандры Амазонки на снимке NASA (MODIS).','Meanders of the Amazon in a NASA MODIS image.'),
 ('07-tundra','tundra','07','## 7.8. ','Тундра осенью у озера Ловозеро (Мурманская область).','Tundra in autumn near Lake Lovozero (Murmansk Region).'),
 ('07-taiga','taiga','07','## 7.8. ','Тайга в Саянских горах (Красноярский край): хвойный лес умеренного пояса.','Taiga in the Sayan Mountains (Krasnoyarsk Krai): coniferous forest of the cool temperate zone.'),
 ('07-steppe','steppe','07','## 7.8. ','Степь в Монголии: бескрайние травы, деревьев почти нет.','Steppe in Mongolia: endless grasses and almost no trees.'),
 ('07-savanna','savanna','07','## 7.8. ','Саванна с акациями в Кении.','A savanna with acacias in Kenya.'),
 ('07-desert','sahara','07','## 7.8. ','Песчаные дюны в пустыне Сахара.','Sand dunes in the Sahara Desert.'),
 ('07-rainforest','rainforest','07','## 7.8. ','Влажный тропический лес (Таиланд).','Tropical rainforest (Thailand).'),
 ('08-soil','soil-profile','08','## 8.3. ','Почвенный профиль с горизонтами.','A soil profile with horizons.'),
 ('08-chernozem','chernozem','08','## 8.7. ','Чернозём — тёмная почва степей с мощным гумусовым горизонтом.','Chernozem, the dark steppe soil with a thick humus horizon.'),
 ('11-terraces','rice-terraces','11','## 11.7. ','Рисовые террасы Лунцзи (Китай): люди превращают склоны в поля.','Longji rice terraces (China): people turn slopes into fields.'),
 ('11-wind','wind-farm','11','## 11.8. ','Ветровая электростанция (США).','A wind farm (USA).'),
 ('11-port','port-of-miami','11','## 11.9. ','Контейнерный порт Майами: морские порты — узлы мировой торговли.','The container port of Miami: seaports are nodes of world trade.'),
 ('12-everest','everest','12','## 12.5. ','Эверест и Гималаи, Азия.','Everest and the Himalayas, Asia.'),
 ('13-smog','smog','13','## 13.3. ','Смог над городом Солт-Лейк-Сити (США).','Smog over Salt Lake City (USA).'),
 ('13-deforest','deforestation-rondonia','13','## 13.7. ','Вырубка и пожары в штате Рондония (Бразилия), снимок NASA.','Deforestation and fires in Rondônia (Brazil), a NASA image.'),
 ('13-aral','aral-ships','13','## 13.8. ','Кладбище кораблей в Муйнаке: на месте Аральского моря осталась пустыня.','The ship graveyard at Muynak: a desert is left where the Aral Sea used to be.'),
 ('15-landsat','landsat','15','## 15.5. ','Снимок Landsat в естественных цветах (NASA).','A Landsat true-colour image (NASA).'),
 ('16-compass','compass','16','## 16.3. ','Старинный судовой компас в кардановом подвесе.','An old ship’s compass in gimbals.'),
 ('16-theodolite','theodolite','16','## 16.3. ','Теодолит — прибор для измерения углов на местности.','A theodolite, an instrument for measuring angles on the ground.'),
 ('16-ptolemy','ptolemy-map','16','## 16.9. ','Карта мира по Птолемею, издание Ульма, 1482 г.','Ptolemy’s world map, Ulm edition, 1482.'),
]
# slot-ы-дубликаты (одна фотография в двух местах) берут метаданные оригинала
ALIAS = {'24-walnut': '21-walnut', '24-burana': '25-burana', '25-bishkek': '24-bishkek', '20-kelsuu': '22-kelsuu'}
# корректные отображаемые имена авторов (если в метаданных мусор)
AUTH = {}
PD = {'Public domain': 'общественное достояние', 'CC0': 'CC0'}
PD_EN = {'Public domain': 'public domain', 'CC0': 'CC0'}


def main():
    meta = json.load(open(os.path.join(SRC, 'atlas_meta.json'), encoding='utf-8'))
    meta2 = json.load(open(os.path.join(SRC, 'atlas_meta2.json'), encoding='utf-8'))
    meta.update(meta2)
    os.makedirs(OUT, exist_ok=True)
    made = {}
    for slot, name, ch, head, cru, cen in D:
        key = ALIAS.get(slot, slot)
        m = meta[key]
        fn = f'{ch}-{name}.jpg'
        dst = OUT + fn
        if not os.path.exists(dst):
            cand = [os.path.join(SRC, f'atlas_{"new_" if key in meta2 else ""}{key}.{e}') for e in ('jpg', 'png')]
            sp = next((c for c in cand if os.path.exists(c)), None)
            if not sp:
                print('NO FILE', slot); continue
            im = Image.open(sp).convert('RGB')
            if im.width > 1600:
                im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
            if im.height > 1200:
                im = im.resize((round(im.width * 1200 / im.height), 1200), Image.LANCZOS)
            q = 82
            while True:
                im.save(dst, 'JPEG', quality=q, optimize=True, progressive=True)
                if os.path.getsize(dst) <= 380_000 or q <= 60: break
                q -= 4
            made[slot] = (im.size, os.path.getsize(dst))
        # подпись
        au = AUTH.get(key) or m['artist'].split('\n')[0].strip()
        au = re.sub(r'\s+', ' ', au)
        lic = m['lic']
        page = m['page'].replace('(', '%28').replace(')', '%29')
        lru = PD.get(lic, lic); len_ = PD_EN.get(lic, lic)
        link = f'[Wikimedia Commons]({page})'
        cap = f'*{cru} Фото: {au}, {lru}, {link} / {cen} Photo: {au}, {len_}, {link}.*'
        alt = f'{cru.split(".")[0]} / {cen.split(".")[0]}'
        p = glob.glob(CH + ch + '-*.md')[0]
        lines = open(p, encoding='utf-8').read().split('\n')
        if any(f'photos/{fn}' in l for l in lines):
            continue
        idx = [i for i, l in enumerate(lines) if l.startswith(head)]
        assert idx, (slot, head)
        i = idx[0]
        lines[i + 1:i + 1] = ['', f'![{alt}](../assets/photos/{fn})', '', cap]
        open(p, 'w', encoding='utf-8').write('\n'.join(lines))
    print('сжато:', len(made))
    for s, v in made.items():
        print(s, v)


if __name__ == '__main__':
    main()
