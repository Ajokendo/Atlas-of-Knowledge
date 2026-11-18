# -*- coding: utf-8 -*-
"""Дополнительные JS-помощники: графики, геометрия, форматирование."""
MJS2 = r'''
function fnum(v,dp){let r=Math.round(v*Math.pow(10,dp==null?2:dp))/Math.pow(10,dp==null?2:dp);if(Object.is(r,-0))r=0;const s=String(r);return lang==="ru"?s.replace(".",","):s}
function Gr(o){const l0=o.L==null?50:o.L,t0=o.T==null?15:o.T,W=o.W||500,H=o.H||210,cid="cg"+(Gr.n=(Gr.n||0)+1);
 const X=v=>l0+(v-o.x0)/(o.x1-o.x0)*W,Y=v=>t0+H-(v-o.y0)/(o.y1-o.y0)*H;
 return {X:X,Y:Y,
  grid:function(sx,sy,lab){let s='<defs><clipPath id="'+cid+'"><rect x="'+l0+'" y="'+t0+'" width="'+W+'" height="'+H+'"/></clipPath></defs>';sx=sx||1;sy=sy||1;
   for(let v=Math.ceil(o.x0/sx-1e-9)*sx;v<=o.x1+1e-9;v+=sx){s+=L(X(v),t0,X(v),t0+H,Math.abs(v)<1e-9?COL.ink:"#e3e1da",Math.abs(v)<1e-9?1.6:1);if(lab!==false)s+=TX(X(v),Math.min(t0+H+14,Y(0)+14),fnum(v),COL.mut,10)}
   for(let v=Math.ceil(o.y0/sy-1e-9)*sy;v<=o.y1+1e-9;v+=sy){s+=L(l0,Y(v),l0+W,Y(v),Math.abs(v)<1e-9?COL.ink:"#e3e1da",Math.abs(v)<1e-9?1.6:1);if(lab!==false&&Math.abs(v)>1e-9)s+=TX(Math.max(l0-4,X(0)-4),Y(v)+4,fnum(v),COL.mut,10,"end")}
   return s},
  fn:function(f,col,w,a,b,dash){let d="",pen=false;const A=a==null?o.x0:a,B=b==null?o.x1:b,rg=o.y1-o.y0;
   for(let i=0;i<=400;i++){const x=A+(B-A)*i/400,y=f(x);if(!isFinite(y)||Math.abs(y-(o.y0+o.y1)/2)>3*rg){pen=false;continue}d+=(pen?"L":"M")+X(x).toFixed(1)+" "+Y(y).toFixed(1)+" ";pen=true}
   return '<g clip-path="url(#'+cid+')"><path d="'+d+'" fill="none" stroke="'+(col||COL.a)+'" stroke-width="'+(w||2.5)+'"'+(dash?' stroke-dasharray="6 5"':"")+'/></g>'},
  pt:function(x,y,col,r){return C(X(x),Y(y),r||5,col||COL.a)},
  seg:function(x1,y1,x2,y2,col,w){return L(X(x1),Y(y1),X(x2),Y(y2),col||COL.ink,w||1.5)},
  txt:function(x,y,t,col,sz,anc){return TX(X(x),Y(y),t,col||COL.ink,sz||12,anc||"middle")}}}
function poly(pts,fill,stroke,sw){return '<polygon points="'+pts.map(p=>p[0].toFixed(1)+","+p[1].toFixed(1)).join(" ")+'" fill="'+(fill||"none")+'" stroke="'+(stroke||COL.ink)+'" stroke-width="'+(sw||2)+'" stroke-linejoin="round"/>'}
function pline(pts,stroke,sw,dash){return '<polyline points="'+pts.map(p=>p[0].toFixed(1)+","+p[1].toFixed(1)).join(" ")+'" fill="none" stroke="'+(stroke||COL.ink)+'" stroke-width="'+(sw||2)+'"'+(dash?' stroke-dasharray="6 5"':"")+'/>'}
function arcA(cx,cy,r,a0,a1,col,w){const p=a=>[cx+r*Math.cos(a),cy-r*Math.sin(a)];const s=p(a0),e=p(a1);const large=Math.abs(a1-a0)>Math.PI?1:0;return '<path d="M'+s[0].toFixed(1)+" "+s[1].toFixed(1)+" A"+r+" "+r+" 0 "+large+" 0 "+e[0].toFixed(1)+" "+e[1].toFixed(1)+'" fill="none" stroke="'+(col||COL.a)+'" stroke-width="'+(w||2.5)+'"/>'}
function deg(a){return a*Math.PI/180}
function dist(a,b){return Math.hypot(a[0]-b[0],a[1]-b[1])}
function clamp(x,a,b){return Math.min(b,Math.max(a,x))}
function sgn(x){return x>0?"+":x<0?"−":""}
function pn(n,a,b,c){const m=Math.abs(n)%100,k=m%10;return m>10&&m<20?c:k===1?a:k>=2&&k<=4?b:c}
function ruen(n,ruForms,enOne,enMany){return lang==="ru"?n+" "+pn(n,ruForms[0],ruForms[1],ruForms[2]):n+" "+(n===1?enOne:enMany)}
function fact(n){let r=1;for(let i=2;i<=n;i++)r*=i;return r}
function nCr(n,k){if(k<0||k>n)return 0;let r=1;for(let i=1;i<=k;i++)r=r*(n-k+i)/i;return Math.round(r)}
'''
MJS2 += r'''
function supn(e){return String(e).split("").map(c=>"⁰¹²³⁴⁵⁶⁷⁸⁹"[+c]).join("")}
function facStr(n){if(n<2)return String(n);let r=[],p=2,m=n;while(p*p<=m){let e=0;while(m%p===0){m/=p;e++}if(e)r.push(e>1?p+supn(e):""+p);p++}if(m>1)r.push(String(m));return r.join("·")}
function lcm(a,b){return a/gcd(a,b)*b}
function divisors(n){const r=[];for(let i=1;i<=n;i++)if(n%i===0)r.push(i);return r}
function isPrime(n){if(n<2)return false;for(let i=2;i*i<=n;i++)if(n%i===0)return false;return true}
function frStr(n,d){return n+"/"+d}
function mixed(n,d){const w=Math.floor(n/d),r=n%d;return w===0?frStr(n,d):r===0?String(w):w+" "+frStr(r,d)}
'''
MJS2 += r'''
function triSides(a,b,c){if(a+b<=c||a+c<=b||b+c<=a)return null;const x=(b*b+c*c-a*a)/(2*c),y=Math.sqrt(Math.max(0,b*b-x*x));return [[0,0],[c,0],[x,y]]}
function fitPts(P,x0,y0,w,h,keep){const xs=P.map(p=>p[0]),ys=P.map(p=>p[1]),mnx=Math.min(...xs),mxx=Math.max(...xs),mny=Math.min(...ys),mxy=Math.max(...ys);const s=Math.min(w/Math.max(1e-9,mxx-mnx),h/Math.max(1e-9,mxy-mny))*(keep||1);return P.map(p=>[x0+(p[0]-mnx)*s+(w-(mxx-mnx)*s)/2,y0+h-(p[1]-mny)*s-(h-(mxy-mny)*s)/2])}
function angAt(P,i){const A=P[i],B=P[(i+1)%3],C=P[(i+2)%3];const u=[B[0]-A[0],B[1]-A[1]],w=[C[0]-A[0],C[1]-A[1]];return Math.acos(clamp((u[0]*w[0]+u[1]*w[1])/(Math.hypot(...u)*Math.hypot(...w)),-1,1))*180/Math.PI}
'''

MJS2 += r'''
function P3(yaw,pitch,s,cx,cy){const cy_=Math.cos(yaw),sy=Math.sin(yaw),cp=Math.cos(pitch),sp=Math.sin(pitch);return function(x,y,z){const x1=x*cy_-y*sy,y1=x*sy+y*cy_;return [cx+s*x1,cy-s*(z*cp-y1*sp)]}}
function box3(P,pts,edges,col,w){let g="";edges.forEach(e=>{g+=L(P(...pts[e[0]])[0],P(...pts[e[0]])[1],P(...pts[e[1]])[0],P(...pts[e[1]])[1],col||COL.ink,w||2)});return g}
function cross3(a,b){return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]}
function dot3(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]}
function len3(a){return Math.hypot(a[0],a[1],a[2])}
'''
