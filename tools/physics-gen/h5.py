# -*- coding: utf-8 -*-
from gen import *
def LINK(u,t): return '<a href="%s" target="_blank" rel="noopener">%s</a>'%(u,t)
def qz(rq,ok,w1,w2,rx,eq,eok,ew1,ew2,ex):
    return (rq,[(ok,'Верно. '+rx),(w1,'Нет. '+rx),(w2,'Нет. '+rx)],eq,[(eok,'Correct. '+ex),(ew1,'No. '+ex),(ew2,'No. '+ex)],0)
def stdhint(m_ru,m_en): return ('Подсказку даст модель «%s». Разгадка — в конце главы.'%m_ru,'The “%s” model gives a hint. The answer is at the end of the chapter.'%m_en)
def stdnote(extra_ru,extra_en): return ('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. '+extra_ru,'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. '+extra_en)
