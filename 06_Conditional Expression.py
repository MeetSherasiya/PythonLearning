# <----------------pr 1------------------------>
# Write a program to find greatest of four numbers entered by the user.
# <-------------------------------------------->

# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))
# num3 = int(input("Enter Number 3 : "))
# num4 = int(input("Enter Number 4 : "))

# if(num1>num4):
#     f1= num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2= num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) +" " + "is greatest")
# else:
#     print(str(f2) +" " + "is greatest")




# <----------------pr 2------------------------>
# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take makes as an input from the user.
# <-------------------------------------------->

# sub1 = int(input("Enter 1st Subject Marks : "))
# sub2 = int(input("Enter 2nd Subject Marks : "))
# sub3 = int(input("Enter 3rd Subject Marks : "))

# if sub1<33 or sub2<33 or sub3<33:
#     print("You are Fail Because you have less than 33% in one of the subjects")
# elif (sub1 +sub2 + sub3)/3 <40:
#     print("You are Fail due to total percentage less than 40%")
# else:
#     print("You are Pass")



# <----------------pr 3------------------------>
# A spam comment is defined as a text containsing following keywords: "make a lot of money", "buy now", "click this", "subscribe this". write a program to detect these spams.
# <-------------------------------------------->

# text = input("Enter the text\n")
# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")




# <----------------pr 4------------------------>
# Write a program to find whether a given username contains kess than 10 characters or not.
# <-------------------------------------------->

# name = input("Enter the user name :\n")
# len(name)
# if(len(name)<10):
#     print("The Character is less than 10")
# else:
#     print("The Character length is grater than or equal to 10")




# <----------------pr 5------------------------>
# Write a program which finds out whether a given name is present in a list or not.
# <-------------------------------------------->

# names = ["Harry", "Shubham", "Rohit", "Aditi"]
# name = input("Enter the name :\n")

# if name in  names:
#     print("Your name is present in list")
# else:
#     print("Your name is not present in list")



# <----------------pr 6------------------------>
# Write a program to calculate the grade of a student from his makes from the following scheme: 90-100-Ex , 80-90-A , 70-80-B , 60-70-C , 50-60-D , <50-F
# <-------------------------------------------->

# marks = int(input("Enter your marks :\n"))

# if marks>=90:
#     grade = "Ex"
# elif marks>=80:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>=60:
#     grade = "C"
# elif marks>=50:
#     grade = "D"
# else:
#     grade = "F"

# print("Your Grade is " + grade)


# <----------------pr 7------------------------>
# Write a program to find out whether a given post is talking about "Harry" or not.
# <-------------------------------------------->

# text = ("Harry is the youtuber. hARry is a python programer.").lower()
# if str("harry") in text:
#     print("Yes this post is talking about harry.")
# else:
#     print("No this post is not talking about harry.")