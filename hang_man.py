import random
word=[
    "apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat", "ice", "jungle",
    "kite", "lemon", "monkey", "nest", "orange", "pencil", "queen", "rose", "sun", "tree",
    "umbrella", "violin", "wolf", "xylophone", "yogurt", "zebra", "air", "boat", "cloud",
    "drum", "eagle", "fire", "glass", "hill", "ink", "jar", "key", "leaf", "moon", "net",
    "ocean", "paint", "quiet", "river", "star", "tent", "under", "vase", "wind", "xray",
    "yard", "zip", "ball", "cake", "doll", "egg", "frog", "gift", "home", "idea", "joke",
    "king", "lamp", "milk", "nose", "owl", "pizza", "quiz", "rain", "sock", "train", "unit",
    "van", "water", "axe", "belt", "coin", "dust", "engine", "farm", "gold", "iron", "jam",
    "kick", "lion", "man", "oil", "pen", "rope", "ship", "tool", "use", "view", "wall", "zone",
    "nest", "time", "space", "planet", "galaxy", "rocket", "science", "math", "code", "logic",
    "earth", "mars", "venus", "music", "dance", "movie", "dream", "goal", "hope", "smile",
    "laugh", "run", "jump", "swim", "play", "read", "write", "think", "talk", "listen",
    "learn", "build", "create", "explore", "travel", "fly", "drive", "climb", "sing", "draw"
]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives=6
Hang=0
letters=[]
random_word=random.choice(word)
display=["_"]*len(random_word)
print(" ".join(display))
print("")
print(HANGMANPICS[0])
while "_" in display and lives>0 :
    guess=input("\nPlz guess a letter :\n").lower()
    if guess in letters :
        print("You are already guess this letter")
        print("\n plz try with another letter")
        print(f"\nyou have more {lives} lives ")
        continue
    letters.append(guess)

    if guess not in random_word :
        lives-=1
        Hang+=1
        print(HANGMANPICS[Hang])

    for possesion in range(len(random_word)):
        if random_word[possesion]==guess:
            display[possesion]=guess
    print(" ".join(display))
    print(f"You have more {lives} lives")

if lives==0:
    print("***you looose***")
    print(HANGMANPICS[-1])
    print(f"Your word is :{random_word}")
else:
    print("You win the game")

