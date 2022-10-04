# <----------------pr 1------------------------>
# Create two virtual environments, install few packeges in the first one. How do you create a similar environment in the second one?
# <-------------------------------------------->

# virtualenv env1 & virtualenv env2
# path : .\env1\Scripts\active.ps1


# <----------------pr 2------------------------>
# Write a program to input name, marks and phone number of a student and format it using the format function like below: "The name of the student is Harry, his marks are 72 and phone number is 99999888"
# <-------------------------------------------->

# name = input("Enter your name : ")
# marks = input("Enter your marks : ")
# phone = input("Enter your phone number : ")

# template = "The name of student is {}, his marks are {} and phone number is {} ".format(name,marks,phone)
# print(template)


# <----------------pr 3------------------------>
# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers.
# <-------------------------------------------->

# l = [str(i*7) for i in range(1,11)]

# verticalTable = "\n".join(l)
# print(verticalTable)


# <----------------pr 4------------------------>
# Write a program to filter a list of numbers which are divisible by 5.
# <-------------------------------------------->

# l = [4, 6, 24, 65, 35, 7, 60, 5, 15, 86]

# a = filter(lambda a: a%5==0, l)
# print(list(a))


# <----------------pr 5------------------------>
# Write a program to find the maximum of the numbers in a list using the reduce function.
# <-------------------------------------------->

# from functools import reduce

# l = [35, 45, 43, 54, 64, 25, 65, 87, 36, 84]

# a = reduce(max, l)
# print(a)

