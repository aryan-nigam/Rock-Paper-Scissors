import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
print("Comp turn:Rock(r) Paper(p) or Scissors(s)?")
randNo=random.randint(1, 3)
if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='s'

you=input("player's turn:Rock(r) Paper(p) or Scissors(s)?")
a=gameWin(comp,you)
if a==None:
    print("the game is a tie")
elif a:
    print("hurrah!!you win")
else:
    print("your lose!better luck next time")
