from ti_draw import *
from random import *
from ti_system import *
from time import *
time=monotonic()
count=2
offset=time
wx=[]
wy=[]
ww=[]
wh=[]
k=0
score=0
movespeed=((0.1*score)+5)*len(wx)
x=303
y=95
w=15
h=15
scoreup=0
newamount=20
def addnew():
  newwidth=randint(3,10)
  newheight=randint(30,100)
  newx=((randint(-150,-6))-newwidth)
  
  newy=randint(20,(210-newheight))
  wx.append(newx)
  wy.append(newy)
  ww.append(newwidth)
  wh.append(newheight)
addnew()
def new():
  global score
  if (wx[0]+ww[0])>=325:
    set_color(255,255,255)
    fill_rect(wx[0],wy[0],ww[0],wh[0])
    score+=1
    wx.pop(0)
    wy.pop(0)
    ww.pop(0)
    wh.pop(0)
    newwidth=randint(3,10)
    newheight=randint(30,100)
    newy=randint(20,(210-newheight))
    newx=((randint(-150,-6))-newwidth)
    wx.append(newx)
    wy.append(newy)
    ww.append(newwidth)
    wh.append(newheight)
def move():
  for i in range((len(wx))):
    set_color(255,255,255)
    fill_rect(wx[i],wy[i],ww[i],wh[i])
    tempx=wx[i]
    wx.pop(i)
    tempx+=movespeed
    wx.insert(i,tempx)
    set_color(0,0,0)
    fill_rect(wx[i],wy[i],ww[i],wh[i])

def dplay():
  set_color(0,0,0)
  fill_rect(x,y,w,h)

def eplay():
  set_color(255,255,255)
  fill_rect(x,y,w,h)
toggle=True
toggle2=True
draw_text(125,20,"Score: " + str(score))
draw_line(-1,19,320,19)
while True:
  if score>scoreup:
    scoreup=score
    set_color(255,255,255)
    fill_rect(125,0,100,19)
    set_color(0,0,0)
    draw_text(125,20,"Score: " + str(score))
  time=monotonic()
  if time-offset>=1 and toggle:
    toggle=False
    addnew()
  tk=get_key(0)
  if tk!=0:
    
    k=tk
  if movespeed<=20:
    movespeed=((0.03*score)+3)*len(wx)
  for i in range((len(wx))-1):
    if wx[i]+ww[i]>=x and x+w<=wx[i] and y+h>=wy[i] and y<=wy[i]+wh[i]:
      clear()
      disp_clr()
      print("Score: " + str(score))
      sleep(1)
      print("")
      print("Press any key to restart")
      wait_key()
      count=2
      time=monotonic()
      offset=time
      offset2=time
      score=0
      wx.clear()
      wy.clear()
      ww.clear()
      wh.clear()
      addnew()
      wx.pop(0)
      wy.pop(0)
      ww.pop(0)
      wh.pop(0)
      addnew()
      toggle=True
      toggle2=True
      movespeed=((0.1*score)+5)*len(wx)
      draw_text(125,20,"Score: " + str(score))
      draw_line(-1,19,320,19)
  new()
  move()
  eplay()
  if k==25:
    y-=15
  if k==34:
    y+=15
  if y>=210-h:
    y=210-h
  if y<=19:
    y=19
  dplay()
  if score>=newamount and count<3:
    if toggle2:
      offset2=time
      toggle2=False
    if time-offset2>=1:
      newamount=score+20
      addnew()
      toggle2=True
      count=count+1