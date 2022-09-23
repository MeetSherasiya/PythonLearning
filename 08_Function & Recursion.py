# <----------------pr 1------------------------>
# Write a program using function to find greatest of three numbers.
# <-------------------------------------------->

# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m=maximum(12,43,1)
# print("The value of the maximum is " + str(m))





# <----------------pr 2------------------------>
# Write a python program using function to convert celsius to fahrenhit.
# <-------------------------------------------->

# def frah(cel):
#     return (cel *(9/5)) + 32

# c = 0
# f = frah(c)
# print("Fahreheit Temperature is " + str(f))






# <----------------pr 3------------------------>
# How do you prevent a python print() function to print a new line at the end.
# <-------------------------------------------->

# print("Hello", end="\n")
# print("How", end="\n")
# print("are", end="\n")
# print("you?", end=" ")





# <----------------pr 4------------------------>
# Write a recursive function to calculate the sum of first n natural numbers.
# <-------------------------------------------->

# def sum(n):
#     if (n == 0):
#         return 0
#     else:
#         return sum(n-1) + n

# n = int(input("Enter a number : "))
# s = sum(n)
# print("The sum of first n number is " + str(s))





# <----------------pr 5------------------------>
# Write a python function to print first n lines of the following pattern.
# <-------------------------------------------->

# def pattern(n):
#     for i in range(n):
#                         print("*" * (n-i))
# n = 3
# p = pattern(n)





# <----------------pr 6------------------------>
# Write a python function which converts inches to cm.
# <-------------------------------------------->


# def convert(inches):
#     return inches*2.54

# inches = int(input("Enter the inches : "))
# i = convert(inches)
# print("Convert the " + str(inches) + " inches to cm is " + str(i))






# <----------------pr 7------------------------>
# Write a python function to remove a given word from a string and step it at the same time.
# <-------------------------------------------->

# def remove_and_strip(string, word):
#     newStr = string.replace(word, "")
#     return newStr.strip()

# this = "      Harry is a good        "
# n = remove_and_strip(this,"Harry")
# print(n)







# <----------------pr 8------------------------>
# write a python function to print multiplication table of a given number.
# <-------------------------------------------->

# def mul(n):
#     for i in range(1,11):
#         print(n*i)

# num = int(input("Enter a number : "))
# print(mul(num))