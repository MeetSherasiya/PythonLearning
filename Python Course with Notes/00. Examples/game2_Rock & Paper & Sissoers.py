import random

tie = 0
youWin = 0
compWin = 0

def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False

    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True

    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False

while(True):
    randNo = random.randint(1,3)
    if randNo == 1:
        comp = "r"
    elif randNo == 2:
        comp = "p"
    elif randNo == 3:
        comp = "s"

    you = input("You Player : Rock(r) , Papper(p) or Sissoers(s)")
    a = gameWin(comp, you)

    print(f"Computer Choose {comp}")
    print(f"You Choose {you}")


    if a == None:
        print("Game is Tie")
        tie +=1
    elif a:
        print("Game is Win")
        youWin += 1
    else:
        print("Game is Lose")
        compWin += 1

    print(f"Win : {youWin}  Loss : {compWin} Tie : {tie}")

    if you == 'q':
        break


print("Thanks for playing this game")