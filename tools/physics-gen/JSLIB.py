# shared JS helpers for block VII
JSL = r'''
const U=(r,e)=>lang==="ru"?r:e;
function sci(x,dp){if(!isFinite(x)||x===0)return"0";const e=Math.floor(Math.log10(Math.abs(x)));let m=x/Math.pow(10,e);let s=fmt(m,dp==null?1:dp);if(parseFloat(s.replace(",","."))>=10){m/=10;s=fmt(m,dp==null?1:dp);return s+"·10"+sup(e+1)}return s+"·10"+sup(e)}
function sup(e){return String(e).split("").map(c=>c==="-"?"⁻":"⁰¹²³⁴⁵⁶⁷⁸⁹"[+c]).join("")}
function hue(l){return l<380?"#6a3d9a":l>750?"#7a1f1f":"hsl("+(270-(l-380)/370*270)+",90%,50%)"}
'''
