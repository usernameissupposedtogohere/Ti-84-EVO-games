from ti_system import *
disp_clr()
from time import *
from random import *
from ti_draw import *
print("Dodge red blocks")
print("")
print("Each red block that touches theground gives one point")
print("")
print("")
print("Press any key to continue")
wait_key()
disp_clr()
print("Use left and right arrow keys  to move")
print("")
print("Use up arrow to stay still")
print("")
print("The map loops pac-man style")
print("")
print("")
print("Press any key to start")
FLBLKBST=[]
wait_key()
name="BEST"
best=recall_list(name)
FLBLKBST.append(best[0])

over=False

e1h=35
e1w=35
e1s=9

e2h=35
e2w=35
e2s=8

e3h=35
e3w=35
e3s=7

e4h=35
e4w=35
e4s=6

e5h=35
e5w=35
e5s=5

e1y=-24
e1x=randint(0,294)
e2y=-24
e2x=randint(0,294)
e3y=-24
e3x=randint(0,294)
e4x=randint(0,294)
e4y=-24
e5x=randint(0,294)
e5y=-24
score=0
draw_text(0,18,str(score))
efef=score
px=160
py=190
ph=15
pw=15
ps=3.4
def clr():
  set_color(255,255,255)
  fill_rect(px,py,pw,ph)
  fill_rect(e1x,e1y,e1w,e1h)
  fill_rect(e2x,e2y,e2w,e2h)
  fill_rect(e3x,e3y,e3w,e3h)
  fill_rect(e4x,e4y,e4w,e4h)
  fill_rect(e5x,e5y,e5w,e5h)
def draw():
  global efef
  set_color(0,0,255)
  fill_rect(px,py,pw,ph)
  set_color(255,0,0)
  fill_rect(e1x,e1y,e1w,e1h)
  fill_rect(e2x,e2y,e2w,e2h)
  fill_rect(e3x,e3y,e3w,e3h)
  fill_rect(e4x,e4y,e4w,e4h)
  fill_rect(e5x,e5y,e5w,e5h)
  if efef!=score:
    set_color(255,255,255)
    fill_rect(0,0,30,20)
    set_color(0,0,0)
    draw_text(0,18,str(score))
    efef=score
while True:
  draw()
  k=get_key(1)
  clr()
  if k==24:
    px=px-ps
  if k==26:
    px=px+ps
  if px>304:
    px=0
  if px<0:
    px=304
  
  if e1y>219:
    e1y=-24
    e1x=randint(0,294)
    score=score+1
  if e2y>219:
    e2y=-24
    e2x=randint(0,294)
    score=score+1
  if e3y>219:
    e3y=-24
    e3x=randint(0,294)
    score=score+1
  if e4y>219:
    e4y=-24
    e4x=randint(0,294)
    score=score+1
  if e5y>219:
    e5y=-24
    e5x=randint(0,294)
    score=score+1
  e1s=(0.04*score)+9
  e2s=(0.04*score)+8
  e3s=(0.04*score)+7
  e4s=(0.04*score)+6
  e5s=(0.04*score)+5
  
  e1y=e1y+e1s
  e2y=e2y+e2s
  e3y=e3y+e3s
  e4y=e4y+e4s
  e5y=e5y+e5s
  
  if e1x<px+pw and e1x+e1w>px and e1y<py+ph and e1y+e1h>py:
    over=True
  if e2x<px+pw and e2x+e2w>px and e2y<py+ph and e2y+e2h>py:
    over=True
  if e3x<px+pw and e3x+e3w>px and e3y<py+ph and e3y+e3h>py:
    over=True
  if e4x<px+pw and e4x+e4w>px and e4y<py+ph and e4y+e4h>py:
    over=True
  if e5x<px+pw and e5x+e5w>px and e5y<py+ph and e5y+e5h>py:
    over=True
  if FLBLKBST and FLBLKBST[0]<score:
    FLBLKBST.pop(0)
    best=score
    FLBLKBST.append(best)
    store_list(name,FLBLKBST)
    FLBLKBST.pop(0)
  if over:
    clear()
    disp_clr()
    e1x=randint(0,294)
    e2x=randint(0,294)
    e3x=randint(0,294)
    e4x=randint(0,294)
    e5x=randint(0,294)
    e1y=-24
    e2y=-24
    e3y=-24
    e4y=-24
    e5y=-24
    px=160
    over=False
    print("Score: [" + str(score) + "]")
    print("")
    best=recall_list(name)
    print("Best: " + str(best))
    print("")
    score=0
    sleep(1)
    print("Press any key to restart")
    wait_key()