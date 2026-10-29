from random import *
from ti_system import *
from ti_draw import *
from time import *
disp_clr()
tickspeeddiv=int(input("Difficulty (ticks/sec): "))
tickspeed=1/tickspeeddiv
disp_clr()
ah=10
aw=10
ax=randrange(0,(308),12)
ay=randrange(0,(198),12)
x=[]
y=[]
w=10
h=10
score=0
xm=12
ym=0
over=False
tempx=0
tempy=0
def newapple():
  global ax
  global ay
  clear_rect(ax,ay,w,h)
  redo=True
  while redo:
    ax=randrange(12,308,12)
    ay=randrange(12,198,12)
    for i in range(len(x)):
      if (ax==x[i] and ay==y[i]):
        ax=randrange(0,(308),12)
        ay=randrange(0,(198),12)
        break
      if i==len(x)-1:
        redo=False
  set_color(255,0,0)
  fill_rect(ax,ay,w,h)
  set_color(0,255,0)
  
def newgame():
  global score
  global over
  global k
  global xm
  global ym
  x.clear()
  y.clear()
  xm=12
  ym=0
  for i in range(4):
    x.append((i*12)+120)
    y.append(84)
  
  clear()
  newapple()
  for i in range(3):
    fill_rect(x[i+1],y[i+1],w,h)
  score=0
  over=False
  k=0
def move():
  global tempx
  global tempy
  global xm
  global ym
  global score
  global over
  global k
  end=False
  if k==45:
    k=get_key(1)
  if k==25 and ym!=12:
    xm=0
    ym=-12
  if k==26 and xm!=-12:
    xm=12
    ym=0
  if k==34 and ym!=-12:
    xm=0
    ym=12
  if k==24 and xm!=12:
    ym=0
    xm=-12
    
  if x[0]>=309 or y[0]>=199 or x[0]<=-1 or y[0]<=-1 and not over:
    over=True
  if x[0]==ax and y[0]==ay:
    tempx=x[0]
    tempx=x[0]
    newapple()
    score+=1
    clear_rect(0,0,40,20)
    set_color(0,0,0)
    draw_text(0,20,str(score))
    end=True
  else:
    tempx=x[0]
    tempy=y[0]
    y.pop(len(y)-1)
    x.pop(len(x)-1)
  toggle=True
  tempx+=xm
  tempy+=ym
  x.insert(0,tempx)
  y.insert(0,tempy)
  set_color(0,125,0)
  fill_rect(x[0],y[0],w,h)
  set_color(0,255,0)
  fill_rect(x[1],y[1],w,h)
  if end:
    fill_rect(x[1],y[1],w,h)
    return 
  set_color(255,255,255)
  fill_rect(x[(len(x)-1)],y[(len(y)-1)],w,h)
  if k!=0:
    fill_rect(x[(len(x)-2)],y[(len(y)-2)],w,h)
newgame()
newapple()
offset=monotonic()
for i in range(4):
  move()
while True:
  if len(x)>=486:
    disp_clr()
    print("You win!")
    sleep(1.5)
    print("")
    print("Press any key to continue")
    wait_key()
    disp_clr()
    tickspeeddiv=int(input("Difficulty (ticks/sec): "))
  if over:
    disp_clr()
    tickspeeddiv=int(input("Difficulty (ticks/sec): "))
    tickspeed=1/tickspeeddiv
    newapple()
    newgame()
    for i in range(5):
      move()
  if k==0:
    k=get_key(0)
  if monotonic()>=offset+tickspeed:
    offset=monotonic()
    move()
    if k==0:
      for i in range(len(x)-1):
        if x[0]==x[i+1] and y[0]==y[i+1]:
          over=True
    k=0
