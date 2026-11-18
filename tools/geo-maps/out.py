import os,json
OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams'
REG=json.load(open('/home/claude/geo/reg.json')) if os.path.exists('/home/claude/geo/reg.json') else {}
def save(id_,slug,ru,en,desc_ru,desc_en,svg,cap_ru,cap_en,alt_ru=None,alt_en=None):
    fn=f'{id_}-{slug}-bilingual.svg'
    open(os.path.join(OUT,fn),'w').write(svg)
    REG[id_]={'file':fn,'alt':(alt_ru or desc_ru)+' / '+(alt_en or desc_en),'cap':f'*{id_}. {cap_ru} / {cap_en}*'}
    json.dump(REG,open('/home/claude/geo/reg_%s.json'%id_[:2],'w') if False else open('/home/claude/geo/reg.json','w'),ensure_ascii=False,indent=1)
