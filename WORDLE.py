from random import *
from time import *
from ti_system import *
from ti_draw import *
tries=0
words=[]
words.extend(["apple", "brave", "chair", "dream", "eagle", "frame", "grape", "horse", "ideal", "jelly", "knife", "lemon", "mango", "night", "ocean", "plane", "queen", "river", "snake", "tiger", "ultra", "vivid", "wings", "xenon", "yacht", "zebra", "angel", "blaze", "candy", "daisy", "early", "fable", "glory", "hairy", "ivory", "jolly", "karma", "latch", "magic", "novel", "olive", "piano", "quake", "raven", "sunny", "tulip", "under", "venom", "whale", "xylem", "young", "zesty", "arise", "bacon", "coral", "demon", "elite", "fence", "giant", "happy", "image", "jewel", "kings", "lunar", "melon", "mouse", "opera", "prime", "quest", "royal", "sweet", "trend", "unity", "vigor", "worry", "xerox", "yield", "zilch", "adore", "binge", "cider", "diver", "entry", "frame", "grind", "hover", "inbox", "joint", "kiosk", "lodge", "might", "night", "outer", "plaza", "quill", "resin", "salsa", "torch", "umbra", "vapor", "widen", "xenon", "youth", "shred", "alien", "beach", "cabin", "debug", "ember", "froze", "grail", "hatch", "idler", "jumps", "knife", "laugh", "mirth", "nerve", "oasis", "pixel", "qualm", "roast", "spike", "thump", "union", "vivid", "wharf", "xenon", "yells", "zappy", "agate", "bland", "crisp", "drape", "exile", "frost", "glide", "honey", "inlet", "jeans", "kneed", "latch", "mango", "nodes", "overt", "pride", "quark", "resin", "salty", "tango", "upset", "vocal", "woven", "xenon", "yours", "zilch", "anise", "binge", "cigar", "delta", "elope", "fancy", "glint", "hover", "inbox", "junta", "kempt", "lucky", "might", "novel", "ombre", "plaza", "quirk", "rover", "sugar", "tulip", "usher", "vigor", "whale", "xenon", "yacht", "zebra", "alloy", "baker", "candy", "drunk", "ember", "flame", "grasp", "hound", "irony", "joint", "knife", "lunar", "magic", "nifty", "ocean", "prism", "quota", "river", "spine", "tango", "upper", "vapor", "wrist", "xerox", "young", "zesty", "alley", "basil", "camel", "daisy", "eager", "fable", "glory", "hazel", "ivory", "juicy", "karma", "lemon", "moist", "nylon", "olive", "plaza", "queen", "roast", "smile", "tiger", "unite", "vivid", "waltz", "xenon", "yield", "zippy", "arbor", "blaze", "cider", "drain", "elite", "fancy", "gloom", "hatch", "inlet", "jewel", "kappa", "loyal", "mirth", "noble", "oasis", "prime", "quill", "risky", "spear", "trout", "upset", "vicar", "woven", "xeric", "yummy", "zebra"])
letters=[]
wasguessed=[]
for i in range(26):
  wasguessed.append(False)
def resetletters():
  letters.clear()
  letters.extend(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
resetletters()
pk=0
checkword=""
wordguess=""
px=5
py=-20

a=False
b=False
c=False
d=False
e=False
f=False
g=False
h=False
i=False
j=False
k=False
l=False
m=False
n=False
o=False
p=False
q=False
r=False
s=False
t=False
u=False
v=False
w=False
x=False
y=False
z=False
def resetalphabet():
  global a
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  global i
  global j
  global k
  global l
  global m
  global n
  global o 
  global p
  global q
  global r
  global s
  global t
  global u
  global v
  global w
  global x
  global y
  global z
  a=False
  b=False
  c=False
  d=False
  e=False
  f=False
  g=False
  h=False
  i=False
  j=False
  k=False
  l=False
  m=False
  n=False
  o=False
  p=False
  q=False
  r=False
  s=False
  t=False
  u=False
  v=False
  w=False
  x=False
  y=False
  z=False
resetalphabet()
def alphabet():
  global a
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  global i
  global j
  global k
  global l
  global m
  global n
  global o
  global p
  global q
  global r
  global s
  global t
  global u
  global v
  global w
  global x
  global y
  global z
  global tpx
  global tpy
  global wordguess
  for ab in range(26):
    
    if ab==0 and "a" in wordguess:
      a=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,a)
    if ab==1 and "b" in wordguess:
      b=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,b)
    if ab==2 and "c" in wordguess:
      c=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,c)
    if ab==3 and "d" in wordguess:
      d=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,d)
    if ab==4 and "e" in wordguess:
      e=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,e)
    if ab==5 and "f" in wordguess:
      f=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,f)
    if ab==6 and "g" in wordguess:
      g=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,g)
    if ab==7 and "h" in wordguess:
      h=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,h)
    if ab==8 and "i" in wordguess:
      i=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,i)
    if ab==9 and "j" in wordguess:
      j=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,j)
    if ab==10 and "k" in wordguess:
      k=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,k)
    if ab==11 and "l" in wordguess:
      l=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,l)
    if ab==12 and "m" in wordguess:
      m=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,m)
    if ab==13 and "n" in wordguess:
      n=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,n)
    if ab==14 and "o" in wordguess:
      o=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,o)
    if ab==15 and "p" in wordguess:
      p=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,p)
    if ab==16 and "q" in wordguess:
      q=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,q)
    if ab==17 and "r" in wordguess:
      r=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,r)
    if ab==18 and "s" in wordguess:
      s=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,s)
    if ab==19 and "t" in wordguess:
      t=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,t)
    if ab==20 and "u" in wordguess:
      u=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,u)
    if ab==21 and "v" in wordguess:
      v=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,v)
    if ab==22 and "w" in wordguess:
      w=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,w)
    if ab==23 and "x" in wordguess:
      x=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,x)
    if ab==24 and "y" in wordguess:
      y=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,y)
    if ab==25 and "z" in wordguess:
      z=True
      wasguessed.pop(ab)
      wasguessed.insert(ab,z)
  
  tpx=140
  tpy=0
  for i in range(26):
    set_color(0,0,0)
    draw_rect(tpx,tpy,20,20)
    if wasguessed[i]:
      set_color(150,0,0)
    else:
      set_color(0,0,150)
    templetter=letters[i]
    draw_text((tpx+5),(tpy+20),templetter)
    tpx+=20
    if tpx>=320:
      tpx=140
      tpy+=20
  set_color(0,0,0)
def grid():
  py=-20
  px=0
  for i in range(6):
    py+=20
    px=5
    for j in range(5):
      draw_rect(px,py,20,20)
      px+=20
correct=False
while True:
  
  wordselect=randint(0,199)
  word=words[wordselect]
  clear()
  grid()
  alphabet()
  px=10
  py=20
  while wordguess!=word and tries<6:
    
    wordguess=""
    while word!=checkword:
      
      if pk==23:
        wordguess=wordguess[:(len(wordguess)-1)]
        set_color(255,255,255)
        fill_rect(0,(py-20),100,20)
        set_color(0,0,0)
        grid()
      if len(wordguess)>=5:
        pk=0
      if pk==41:
        wordguess+="a"
      if pk==42:
        wordguess+="b"
      if pk==43:
        wordguess+="c"
      if pk==51:
        wordguess+="d"
      if pk==52:
        wordguess+="e"
      if pk==53:
        wordguess+="f"
      if pk==54:
        wordguess+="g"
      if pk==55:
        wordguess+="h"
      if pk==61:
        wordguess+="i"
      if pk==62:
        wordguess+="j"
      if pk==63:
        wordguess+="k"
      if pk==64:
        wordguess+="l"
      if pk==65:
        wordguess+="m"
      if pk==71:
        wordguess+="n"
      if pk==72:
        wordguess+="o"
      if pk==73:
        wordguess+="p"
      if pk==74:
        wordguess+="q"
      if pk==75:
        wordguess+="r"
      if pk==81:
        wordguess+="s"
      if pk==82:
        wordguess+="t"
      if pk==83:
        wordguess+="u"
      if pk==84:
        wordguess+="v"
      if pk==85:
        wordguess+="w"
      if pk==91:
        wordguess+="x"
      if pk==92:
        wordguess+="y"
      if pk==93:
        wordguess+="z"
      set_color(255,255,255)
      fill_rect(0,(py-20),100,20)
      set_color(0,0,0)
      grid()
      for i in range((len(wordguess))):
        draw_text(px,py,wordguess[i])
        px+=20
      px=10
      pk=get_key(1)
      if len(wordguess)==5 and pk==105:
        for i in range(5):
          letters.append(wordguess[i])
        alphabet()
        
        
        
        
        checkword=wordguess
        wordguess=""
        py+=20
        if checkword==word:
          correct=True
        break
    for i in range(5):
      gx=(20*i)+10
      checkletter=checkword[i]
      if checkletter in word:
        set_color(255,255,0)
        fill_rect((gx-5),(py-40),20,20)
        set_color(0,0,0)
      draw_text(gx,(py-20),checkword[i])
    for i in range(5):
      gx=(20*i)+10
      if checkword[i]==word[i]:
        set_color(0,255,0)
        fill_rect((gx-5),(py-40),20,20)
        set_color(0,0,0)
        draw_text(gx,(py-20),checkword[i])
    if correct:
      set_color(0,0,0)
      draw_text(100,150,"You got it.")
      draw_text(50,170,"Press any key to restart.")
      
      tries=0
      py=20
      px=10
      pk=0
      checkword=""
      word=""
      wordguess=""
      wasguessed=[]
      for i in range(26):
        wasguessed.append(False)
      letters=[]
      resetletters()
      resetalphabet()
      alphabet()
      wait_key()
      clear()
      tries=0
      break
    tries+=1
    checkword=""
  if not correct:
    draw_text(60,150,("You lost. It was " + word))
    draw_text(50,190,"Press any key to restart.")
    wait_key()
    wasguessed=[]
    for i in range(26):
      wasguessed.append(False)
  tries=0
  letters=[]
  resetletters()
  resetalphabet()
  alphabet()
  py=20
  px=10
  pk=0
  correct=False
  checkword=""
  word=""
  wordguess=""
  correct=False
