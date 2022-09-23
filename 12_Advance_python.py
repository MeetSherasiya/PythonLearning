# <----------------pr 1------------------------>
# Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.
# <-------------------------------------------->

# def readFile(filename):
#     try:
#         with open(filename, "r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"File {filename} is not found.")

# readFile("txt_12pr/1.txt")
# readFile("txt_12pr/2.txt")
# readFile("txt_12pr/3.txt")


# <----------------pr 2------------------------>
# Write a program to print third, fifth and seventh element from a list using enumerate function.
# <-------------------------------------------->

# l = [1, 4, 6, 7, 42, 52, 64, 26, 33, 58]
# for index, item in enumerate(l):
#     if index==2 or index==4 or index==6:
#         print(f"The {index+1}th element is {item}")



# <----------------pr 3------------------------>
# Write a list comprehension to print a list which contains the multiplication table of a user entered number.
# <-------------------------------------------->

# num = int(input("Enter Your Number : "))

# table = [num*i for i in range(1,11)]
# print(table)



# <----------------pr 4------------------------>
# Write a program to display a/b where a and b are integers. If b=0, display infinte by handling the zerodivisionerror.
# <-------------------------------------------->

# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# try:
#     print(a/b)
# except:
#     print("Infinite")



# <----------------pr 5------------------------>
# Store the multiplication tables genrated in problem 3 in a file named Tables.txt.
# <-------------------------------------------->

# num = int(input("Enter Your Number : "))

# table = [num*i for i in range(1,11)]
# print(table)
# with open("txt_12pr/Tables.txt", "a") as f:
#     f.write(f"Table of {num}\n")
#     f.write(str(table))
#     f.write('\n')