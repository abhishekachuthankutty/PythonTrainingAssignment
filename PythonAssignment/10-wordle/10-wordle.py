import random
from click import style
from colorama import Fore, Back, Style
from sqlalchemy import true

def isWordFound(hiddenWord,b):
    if(len(b)!=5):
        return False
    i = 0
    while(i < len(hiddenWord)):
        if(hiddenWord[i]==b[i]):
            hiddenWordFoundList[i] = True
        i+=1
    if(hiddenWord==b):
        return True
    else:
        return False

def isWordValid(w):
    if(len(w)!=5):
        return False
    for item in words:
        if item == w:
            return True
    return False 

def isLetterIn(c):
    return c

f = open("valid-wordle-words.txt")
x = f.readlines()
words = []
for item in x:
    words.append(item.rstrip("\n"))

selectedWord = random.choice(words)

print(Style.BRIGHT+'WORDLE', end="")
print(Style.RESET_ALL)
print('Guess The Word!')
chances = 7
guessed = False
word = []
previousWord = []
hiddenWord = list(selectedWord.strip(" "))
hiddenWordFoundList = []

for item in hiddenWord:
    hiddenWordFoundList.append(False)

while(chances > 0) and (guessed == False):
    i = 0
    invalid = False
    x = input("Enter a word: ")
    y = list(x.strip(" "))
    if(isWordValid(x)):
        chances-=1
    else:
        print("Invalid Word")
        invalid = True
    if(invalid == False):
        guessed = isWordFound(hiddenWord,list(x.strip(" ")))
    while(i < len(hiddenWord)):
        if invalid == True:
            break
        if ((hiddenWordFoundList[i] == True) and (hiddenWord[i] == y[i])):
            print(Back.GREEN+y[i],end="")
            print(Style.RESET_ALL, end=" ")
        elif(y[i] in hiddenWord):
            print(Back.YELLOW+y[i], end="")
            print(Style.RESET_ALL, end=" ")
        else:
            print(Back.WHITE+y[i],end="")
            print(Style.RESET_ALL, end=" ")
        i+=1
    print(Style.RESET_ALL)
    previousWord = y
if(chances == 0 and guessed == False):
    print("Sorry, The correct word was")
    i = 0
    while(i < len(hiddenWord)):
        print(Back.GREEN+hiddenWord[i],end="")
        print(Style.RESET_ALL, end=" ")
        i+=1
    print(Style.RESET_ALL)
if(guessed==True):
    print("Congrats u guessed the coorect word. It was")
    i = 0
    while(i < len(hiddenWord)):
        print(Back.GREEN+hiddenWord[i],end="")
        print(Style.RESET_ALL, end=" ")
        i+=1
    print(Style.RESET_ALL)
       