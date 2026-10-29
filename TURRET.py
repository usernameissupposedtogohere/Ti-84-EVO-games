from time import *
from math import *
from ti_draw import *
from ti_system import *
from random import *

ofst=monotonic()
score=0
lives=5
ex=[]
ey=[]
ems=2
er=8
for i in range(2):
  ex.append(randrange(-31,351,380))
  ey.append(randint(-50,260))
over=False
bx=155
by=-80

x=155
y=99

lx=145
ly=125

rx=165
ry=125

cx=155
cy=112
degset=20
deg=10
tdeg=radians(deg)
k=0
def rotate():
  global deg
  global k
  global cx
  global cy
  global nx
  global ny
  global nlx
  global nly
  global nrx
  global nry
  global nbx
  global nby
  global tdeg
  if k==24 or k==26:
    set_color(255,255,255)
    fill_poly([nrx,nlx,nx],[nry,nly,ny])
  if k==24:
    deg-=degset
  if k==26:
    deg+=degset
  tdeg=radians(deg)
  nx=cx+(x-cx)*cos(tdeg)-(y-cy)*sin(tdeg)
  ny=cy+(x-cx)*sin(tdeg)+(y-cy)*cos(tdeg)
  
  nly=cy+(lx-cx)*sin(tdeg)+(ly-cy)*cos(tdeg)
  nlx=cx+(lx-cx)*cos(tdeg)-(ly-cy)*sin(tdeg)
  
  nrx=cx+(rx-cx)*cos(tdeg)-(ry-cy)*sin(tdeg)
  nry=cy+(rx-cx)*sin(tdeg)+(ry-cy)*cos(tdeg)
  
  nbx=cx+(bx-cx)*cos(tdeg)-(by-cy)*sin(tdeg)
  nby=cy+(bx-cx)*sin(tdeg)+(by-cy)*cos(tdeg)
  if k==24 or k==26:
    set_color(0,0,0)
    fill_poly([nrx,nlx,nx],[nry,nly,ny])
toggle=False
rotate()
fill_poly([nrx,nlx,nx],[nry,nly,ny])
draw_text(70,20,"Lives: "+str(lives)+" Score: "+str(score))
while True:
  if monotonic()>=ofst+0.1 and toggle:
    ofst=monotonic()
    set_color(255,255,255)
    draw_line(nx,ny,nbx,nby)
    set_color(0,0,0)
    fill_poly([nrx,nlx,nx],[nry,nly,ny])
    toggle=False
    k=0
  
  k=get_key(0)
  rotate()
  if k==105:
    draw_line(nx,ny,nbx,nby)
    toggle=True
  for i in range(len(ex)):
    set_color(255,255,255)
    fill_circle(ex[i],ey[i],er)
    if ex[i]<cx:
      ex[i]=ex[i]+(ems+1)
    else:
      ex[i]=ex[i]-(ems+1)
    if ey[i]>cy:
      ey[i]=ey[i]-ems
    else:
      ey[i]=ey[i]+ems
  set_color(0,0,0)
  for i in range(len(ex)):
    fill_circle(ex[i],ey[i],er)
    if sqrt((ex[i]-cx)**2+(ey[i]-cy)**2)<=8:
      lives-=1
      set_color(255,255,255)
      clear_rect(70,0,200,20)
      fill_circle(ex[i],ey[i],er)
      set_color(0,0,0)
      draw_text(70,20,"Lives: "+str(lives)+" Score: "+str(score))
      fill_poly([nrx,nlx,nx],[nry,nly,ny])
      ex.pop(i)
      ey.pop(i)
      ex.insert(i,randrange(-31,351,380))
      ey.insert(i,randint(-50,260))
      if lives<=0:
        clear()
        disp_clr()
        print("Score: "+str(score))
        sleep(1)
        print("Press any key to restart")
        wait_key()
        lives=5
        score=0
        k=7
        
        draw_text(70,20,"Lives: "+str(lives)+" Score: "+str(score))
        ex=[]
        ey=[]
        for i in range(2):
          ex.insert(i,randrange(-31,351,380))
          ey.insert(i,randint(-50,260))
        deg=10
        k=7
        rotate()
        fill_poly([nrx,nlx,nx],[nry,nly,ny])
    dx=nx-nbx
    dy=ny-nby
    l2=dx*dx+dy*dy
    t=((ex[i]-nbx)*dx+(ey[i]-nby)*dy)/l2
    t=max(0.0, min(1.0, t))
    closex=nbx+t*dx
    closey=nby+t*dy
    distsq=(ex[i]-closex)**2+(ey[i]-closey)**2
    if distsq<=er*er and k==105:
      set_color(255,255,255)
      fill_circle(ex[i],ey[i],er)
      set_color(0,0,0)
      
      ex[i]=randrange(-31,351,380)
      ey[i]=randint(-50,260)
      score+=1
      clear_rect(70,0,200,20)
      draw_text(70,20,"Lives: "+str(lives)+" Score: "+str(score))