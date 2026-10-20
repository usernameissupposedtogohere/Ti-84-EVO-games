from random import *
from ti_system import *
from ti_draw import *
keyletters={41:"a",42:"b",43:"c",51:"d",52:"e",53:"f",54:"g",55:"h",61:"i",62:"j",63:"k",64:"l",65:"m",71:"n",72:"o",73:"p",74:"q",75:"r",81:"s",82:"t",83:"u",84:"v",85:"w",91:"x",92:"y",93:"z"}
tries=0
words=[]
words.extend(["crane", "blitz", "flame", "ghost", "proud", "swirl", "knock", "vivid", "charm", "shelf", "trout", "gleam", "spine", "march", "flock", "brave", "nymph", "stark", "plumb", "ocean", "grape", "shiny", "crisp", "thump", "waltz", "smoke", "adopt", "frost", "blush", "crown", "sweep", "dizzy", "piano", "quirk", "stone", "latch", "beach", "prism", "clown", "drift", "sword", "mango", "sneak", "orbit", "paint", "flute", "shark", "brisk", "doubt", "cabin", "spoon", "glory", "wheat", "track", "lemon", "swoop", "creek", "jazzy", "torch", "medal", "plant", "brick", "spice", "cloud", "swing", "tiger", "chess", "pearl", "scoff", "drown", "grind", "honey", "quick", "storm", "wrist", "prank", "sauce", "cider", "angel", "skull", "cruel", "fancy", "spear", "mirth", "glove", "ranch", "pouch", "ivory", "badge", "cough", "shrub", "twist", "vapor", "delta", "caper", "giant", "cello", "kneel", "muddy", "sheep", "flair", "spurt", "widen", "pupil", "zebra", "chase", "dairy", "satin", "lunar", "silly", "crust", "elbow", "tulip", "fable", "siren", "grove", "cubic", "demon", "relic", "hover", "maple", "snarl", "debut", "sushi", "raven", "tidal", "leapt", "vowel", "sugar", "roast", "worry", "pasta", "scout", "linen", "dwarf", "hefty", "coral", "basin", "pixel", "shove", "robin", "medic", "tweak", "lilac", "couch", "fiery", "spade", "nerdy", "stomp", "flood", "brine", "civic", "eagle", "snack", "dodge", "weary", "clamp", "epoch", "motel", "crept", "humid", "onion", "risky", "tease", "paler", "vital", "frown", "skate", "diner", "shale", "crank", "mimic", "penny", "lodge", "thorn", "inlet", "abide", "fetch", "proxy", "haste", "pride", "ruler", "straw", "daisy", "grain", "plaid", "gloom", "slate", "mural", "tasty", "scarf", "noble", "flint", "jolly", "cocoa", "truce", "spoil", "kayak", "moist", "gravy", "bland", "thief", "fizzy", "dread", "sling", "poker", "creed", "amble", "rover", "cumin", "lucky", "shrew", "tango", "umbra", "prone", "coven", "zesty", "mossy", "rhyme"])
letters=[]
wasguessed=[False]*26
def resetletters():
  letters[:]=list("abcdefghijklmnopqrstuvwxyz")
resetletters()
pk=0
checkword=""
wordguess=""
px=5
py=-20
def alphabet():
  global tpx,tpy
  for ch in wordguess:
    wasguessed[ord(ch)-97]=True
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
      if pk in keyletters:
        wordguess+=keyletters[pk]
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
      wasguessed=[False]*26
      letters=[]
      resetletters()
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
    wasguessed=[False]*26
  tries=0
  letters=[]
  resetletters()
  py=20
  px=10
  pk=0
  correct=False
  checkword=""
  word=""
  wordguess=""