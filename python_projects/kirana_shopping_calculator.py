import random

sum = 0
recipt = random.randint(10000,999999)

while(True):
    userInput = input("Enter a price or q for quit :\n")
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print(f"You total bill is {sum}. Thanks for shooping with us. Your recipt is {recipt}")
        break



