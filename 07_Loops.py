# a = [1,2,4,6,53,36,2,4]

# for b in a:
#     print(b)

# for i in range(1,8):
#     print(i)
# else:
#     print("done")



# <----------------pr 1------------------------>
# Write a program to print multiplication table of a given number using for loop.
# <-------------------------------------------->

# num = int(input("Enter a Number : "))
# for i in range(1,11):
#     print(str(num) + "X" + str(i) + "=" + str(num*i))
#     print(f"{num}X{i}={num*i}")
# else:
#     print("Done")



# <----------------pr 2------------------------>
# Write a program to greet all the person names stored in a list l1 and which starts with 5 l1=["Harry", "Soham" , "Sachin" , "Rahul"]
# <-------------------------------------------->

# l1 = ["Harry", "Soham" , "Sachin" , "Rahul"]

# for name in l1:
#     if name.startswith("S"):
#         print("Hello" + name)



# <----------------pr 3------------------------>
# Attempt problem 1 using while loop.
# <-------------------------------------------->


# num = int(input("Enter a Number : "))
# i = 1
# while i<11:
#     print(str(num) + "X" + str(i) + "=" + str(num*i))
#     print(f"{num}X{i}={num*i}")
#     i = i + 1
# else:
#     print("Done")



# <----------------pr 4------------------------>
# Write a program to find whether a given number is prime or not.
# <-------------------------------------------->

# num = int(input("Enter the number : "))
# prime = True
# for i in range(2,num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")




# <----------------pr 5------------------------>
# Write a program to find the sum of first n natural number using while loop.
# <-------------------------------------------->

# num = int(input("Enter a number : "))
# i = 0
# sum = 0
# while i<=num:
#     sum = i + sum
#     i = i + 1
# print(f"The sum of first n number is {sum}")




# <----------------pr 6------------------------>
# Write a program to calculate the factorial of a given number using for loop.
# <-------------------------------------------->


# num = int(input("Enter the number : "))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i

# print(factorial)



# <----------------pr 7------------------------>
# Write a program to print the following star pattern.
# <-------------------------------------------->


# n = 3
# for i in range(3):
#         print(" " * (n-i-1), end="")
#         print("*" * (2*i+1), end="")
#         print(" " * (n-i-1))


# <----------------pr 8------------------------>
# Write a program to print the following star pattern. (num=3)
# <-------------------------------------------->


# num = int(input("Enter the number : "))
# i = 0
# for i in range(num):
#     print("*" * (i+1))


# <----------------pr 9------------------------>
# Write a program to print the following star pattern. (num=3)
# <-------------------------------------------->

# n = int(input("Enter the number : "))
# for i in range(n):
#     for j in range(n):
#         if(i == 0 or i == n-1 or j == n-1 or j == 0):
#             print("*",end=" ")
#         else:
#             print(' ',end=" ")
#     print()





# <----------------pr 10------------------------>
# Write a program to print multiplication table of n using for loop in reversed order.
# <-------------------------------------------->


# num = int(input("Enter a Number : "))
# for i in range(10,0,-1):
#     # print(str(num) + "X" + str(i) + "=" + str(num*i))
#     print(f"{num}X{i}={num*i}")
# else:
#     print("Done")