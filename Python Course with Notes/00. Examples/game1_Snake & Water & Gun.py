import random

def gameWin(comp, you):

    if comp == you:
        return None

    elif comp == 's':
        if you == '2':
            return False
        elif you == '3':
            return True

    elif comp == 'w':
        if you == '1':
            return True
        elif you == '3':
            return False

    elif comp == 'g':
        if you == '1':
            return False
        elif you == '2':
            return True

print("Computer Turn : Snake(s) , Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'


you = input("Player's Turn : Snake(1) , Water(2) or Gun(3)?")
a = gameWin(comp, you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
