# -*- coding: utf-8 -*-
"""Общие JS-помощники для моделей математики (подставляются в начало js главы)."""
MJS = r'''
const U=(r,e)=>lang==="ru"?r:e;
const COL={a:"#b6533f",b:"#3f5f8f",c:"#2f6f5d",d:"#c9a24a",ink:"#18181a",mut:"#66666b",line:"#cfcfc8",bg:"#f2f2ef"};
function R(x,y,w,h,fill,stroke,sw,rx){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+(fill||"none")+'" stroke="'+(stroke||"none")+'" stroke-width="'+(sw||1)+'"'+(rx?' rx="'+rx+'"':"")+'/>'}
function C(x,y,r,fill,stroke,sw){return '<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="'+(fill||"none")+'" stroke="'+(stroke||"none")+'" stroke-width="'+(sw||1)+'"/>'}
function L(x1,y1,x2,y2,col,w){return '<line x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'" stroke="'+(col||COL.ink)+'" stroke-width="'+(w||1)+'"/>'}
function TX(x,y,t,col,size,anchor,weight){return '<text x="'+x+'" y="'+y+'" text-anchor="'+(anchor||"middle")+'" font-family="Inter,sans-serif" font-size="'+(size||14)+'" font-weight="'+(weight||400)+'" fill="'+(col||COL.ink)+'">'+t+'</text>'}
function numLine(x0,x1,y,mn,mx,step,every){let s=L(x0,y,x1,y,COL.ink,2),k=0;for(let v=mn;v<=mx+1e-9;v+=step,k++){const x=x0+(v-mn)/(mx-mn)*(x1-x0),big=(k%(every||1)===0);s+=L(x,y-(big?8:5),x,y+(big?8:5),COL.ink,big?2:1);if(big)s+=TX(x,y+24,String(Math.round(v*1000)/1000),COL.mut,12)}return s}
function px(v,x0,x1,mn,mx){return x0+(v-mn)/(mx-mn)*(x1-x0)}
function gcd(a,b){return b?gcd(b,a%b):Math.abs(a)}
'''
