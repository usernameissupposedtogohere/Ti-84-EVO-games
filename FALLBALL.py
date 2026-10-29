from random import *
from ti_draw import *
from math import *
from ti_system import *
from time import *
ex=randint(4,316)
ey=randint(4,206)
fill_circle(ex,ey,5)
over=False
score=0
draw_text(0,20,str(score))
x=150
y=15
xm=0
ym=1
while True:
  k=get_key(0)
  if k==45:
    k=get_key(1)
  if k==24:
    xm=-4
  if k==25:
    ym=-4
  if k==26:
    xm=4
  set_color(255,255,255)
  fill_circle(x,y,10)
  if x>310:
    over=True
  if x<10:
    over=True
  if y<10:
    over=True
  if y>200:
    over=True
  ym=ym+0.2
  if xm>0:
    xm=xm-(xm/12)
  elif xm<0:
    xm=xm-(xm/12)
  x=x+xm
  y=y+ym
  set_color(255,0,0)
  fill_circle(x,y,10)
  if over:
    over=False
    clear()
    disp_clr()
    print("Score: " + str(score))
    print("Press any key")
    sleep(1)
    wait_key()
    score=0
    x=150
    y=15
    xm=0
    ym=0
    ex=randint(4,316)
    ey=randint(4,206)
    fill_circle(ex,ey,5)
    draw_text(0,20,str(score))
  if sqrt(((ex-x)**2)+(ey-y)**2)<=15:
    score=score+1
    set_color(255,255,255)
    fill_circle(ex,ey,5)
    ex=randint(4,316)
    ey=randint(4,206)
    fill_rect(0,0,30,20)
    set_color(0,0,0)
    fill_circle(ex,ey,5)
    draw_text(0,20,str(score))