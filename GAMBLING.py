from ti_system import *
disp_clr()
from random import *
from ti_draw import *
from time import *
print("If sum of dice is even: host   wins")
print("")
print("If sum of dice is odd: you win")
print("")
print("Press enter to toggle winner    declaration")
print("")
print("Press any key to start")
def runrng():
  global oc1
  global oc2
  oc1=randint(1,6)
  oc2=randint(1,6)
  clear()
  draw_rect(20,20,120,120)
  draw_rect(170,20,120,120)
  if oc1==1 or oc1==3 or oc1==5:
    fill_circle(80,80,10)
  if oc1==3 or oc1==5 or oc1==4 or oc1==6 or oc1==2:
    fill_circle(120,120,10)
    fill_circle(40,40,10)
  if oc1==4 or oc1==6 or oc1==5:
    fill_circle(40,120,10)
    fill_circle(120,40,10)
  if oc1==6:
    fill_circle(40,80,10)
    fill_circle(120,80,10)
  
  if oc2==6:
    fill_circle(270,80,10)
    fill_circle(190,80,10)
  if oc2==4 or oc2==6 or oc2==5 or oc2==3 or oc2==2:
    fill_circle(270,120,10)
    fill_circle(190,40,10)
  if oc2==4 or oc2==6 or oc2==5:
    fill_circle(270,40,10)
    fill_circle(190,120,10)
  if oc2==1 or oc2==3 or oc2==5:
    fill_circle(230,80,10)
k=get_key(1)
yes=2
while True:
  for i in range(8):
    delay=i/8
    runrng()
    if i<=6:
      sleep(delay)
  draw_text(150,190,str((oc1+oc2)))
  if yes==2:
    if (oc1+oc2)%2==0:
      draw_text(135,205,"I win")
    else:
      draw_text(125,205,"You win")
  k=get_key(1)
  if k==105 and yes==2:
    yes=-2
  elif k==105 and yes==-2:
    
    yes=2