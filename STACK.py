from ti_draw import *
from time import *
from ti_system import *
b1=[]
b2=[]
b3=[]
b4=[]
b5=[]
b6=[]
b7=[]
over=False
y1=179
y2=148
y3=117
y4=86
y5=55
y6=24
y7=-7
s=30
def reset():
  global l1
  global l2
  global l3
  global l4
  global l5
  global l6
  global l7
  global score
  for i in range(3):
    b1.append(((i+1)*s))
    b2.append(((i+1)*s))
    b3.append(((i+1)*s))
  for i in range(2):
    b4.append(((i+1)*s))
    b5.append(((i+1)*s))
  for i in range(1):
    b6.append(((i+1)*s))
    b7.append(((i+1)*s))
  
  l1=True
  l2=True
  l3=True
  l4=True
  l5=True
  l6=True
  l7=True
  score=0
  
reset()
score=0
ticksp=1/((score+1)*3)
offset=monotonic()
l1=True
l2=True
l3=True
l4=True
l5=True
l6=True
l7=True
k=0
ms=30
while True:
  ticksp=1/((score+1)*3.5)
  
  if monotonic()>=offset+ticksp:
    offset=monotonic()
    
    if l1:
      clear_rect(0,y1,320,s)
      for i in range(3):
        b1[i]=b1[i]+ms
        if (b1[i]+ms)>=320:
          ms=-ms
          b1[i]=(b1[i]+(3*ms))
        if b1[i]<=0:
          ms=-ms
          b1[i]=(b1[i]+(3*ms))
      for i in range(3):
        fill_rect(b1[i],y1,s,s)
    elif l2:
      clear_rect(0,y2,320,s)
      for i in range(3):
        b2[i]=b2[i]+ms
        if (b2[i]+ms)>=320:
          ms=-ms
          b2[i]=(b2[i]+(3*ms))
        if b2[i]<=0:
          ms=-ms
          b2[i]=(b2[i]+(3*ms))
      for i in range(3):
        fill_rect(b2[i],y2,s,s)
    elif l3:
      clear_rect(0,y3,320,s)
      for i in range(3):
        b3[i]=b3[i]+ms
        if (b3[i]+ms)>=320:
          ms=-ms
          b3[i]=(b3[i]+(3*ms))
        if b3[i]<=0:
          ms=-ms
          b3[i]=(b3[i]+(3*ms))
      for i in range(3):
        fill_rect(b3[i],y3,s,s)
    elif l4:
      clear_rect(0,y4,320,s)
      for i in range(2):
        b4[i]=b4[i]+ms
        if (b4[i]+ms)>=320:
          ms=-ms
          b4[i]=(b4[i]+(2*ms))
        if b4[i]<=0:
          ms=-ms
          b4[i]=(b4[i]+(2*ms))
      for i in range(2):
        fill_rect(b4[i],y4,s,s)
    elif l5:
      clear_rect(0,y5,320,s)
      for i in range(2):
        b5[i]=b5[i]+ms
        if (b5[i]+ms)>=320:
          ms=-ms
          b5[i]=(b5[i]+(2*ms))
        if b5[i]<=0:
          ms=-ms
          b5[i]=(b5[i]+(2*ms))
      for i in range(2):
        fill_rect(b5[i],y5,s,s)
    elif l6:
      clear_rect(0,y6,320,s)
      b6[0]=b6[0]+ms
      if (b6[0]+ms)>=320:
        ms=-ms
        b6[0]=b6[0]+ms
      if b6[0]<=0:
        ms=-ms
        b6[0]=b6[0]+ms
      fill_rect(b6[0],y6,s,s)
    elif l7:
      clear_rect(0,y7,320,s)
      b7[0]=b7[0]+ms
      if (b7[0]+ms)>=320:
        ms=-ms
        b7[0]=b7[0]+ms
      if b7[0]<=0:
        ms=-ms
        b7[0]=b7[0]+ms
      fill_rect(b7[0],y7,s,s)
    else:
      disp_clr()
      print("You win. Score: "+str(score-1))
      wait_key()
      reset()
      offset=monotonic()
  if k==0:
    k=get_key(0)
  if k==105:
    if l1:
      l1=False
    elif l2:
      i1=False
      i2=False
      i3=False
      l2=False
      for i in range(3):
        if b2[0]==b1[i]:
          i1=True
        if b2[1]==b1[i]:
          i2=True
        if b2[2]==b1[i]:
          i3=True
      if not (i1 and i2 and i3):
        over=True
    elif l3:
      i1=False
      i2=False
      i3=False
      l3=False
      for i in range(3):
        if b3[0]==b2[i]:
          i1=True
        if b3[1]==b2[i]:
          i2=True
        if b3[2]==b2[i]:
          i3=True
      if not (i1 and i2 and i3):
        over=True
    elif l4:
      i1=False
      i2=False
      l4=False
      for i in range(3):
        if b4[0]==b3[i]:
          i1=True
      for i in range(3):
        if b4[1]==b3[i]:
          i2=True
      if not (i1 and i2):
        over=True
    elif l5:
      for i in range(2):
        if b4[i]!=b5[i] and b4[-i]!=b5[-i]:
          over=True
      l5=False
    elif l6:
      i1=False
      l6=False
      for i in range(2):
        if b6[0]==b5[i]:
          i1=True
      if not i1:
        over=True
    elif l7:
      if b6[0]!=b7[0]:
        over=True
      l7=False
    k=0
    ms=30
    score+=1
  if over:
    disp_clr()
    print("You lose. Score: "+str(score-1))
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    b5=[]
    b6=[]
    b7=[]
    l1=True
    l2=True
    l3=True
    l4=True
    l5=True
    l6=True
    l7=True
    reset()
    offset=monotonic()
    over=False
    wait_key()
  k=0