# <----------------pr 1------------------------>
# Create a class programmer for storing information of few programmers working at microsoft.
# <-------------------------------------------->

# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
#     def getInfo(self):
#         print(f"The name of the {self.company} programer is {self.name} and the product is {self.product}")

# harry = Programmer("Harry", "Skype")
# Alka = Programmer("Alka", "GitHub")
# harry.getInfo()
# Alka.getInfo()




# <----------------pr 2------------------------>
# Write a class calculator capable of finding square, cube and squareroot of a number.
# <-------------------------------------------->

# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"The value of {self.number} square is {self.number **2}")

#     def squareRoot(self):
#         print(f"The value of {self.number} squareroot is {self.number **0.5}")

#     def cube(self):
#         print(f"The value of {self.number} cube is {self.number **3}")

# a = Calculator(4)
# a.square()
# a.squareRoot()
# a.cube()




# <----------------pr 3------------------------>
# Create a class with a class attributr a; create an object from it and set a directly using object a=0. Does this change the class attribute?
# <-------------------------------------------->

# class Sample:
#     a = "Harry"

# obj = Sample()
# obj.a = "Vikky"

# print(Sample.a)
# print(obj.a)



# <----------------pr 4------------------------>
# Add a static method in problem 2 to geet the user with hello.
# <-------------------------------------------->


# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"The value of {self.number} square is {self.number **2}")

#     def squareRoot(self):
#         print(f"The value of {self.number} squareroot is {self.number **0.5}")

#     def cube(self):
#         print(f"The value of {self.number} cube is {self.number **3}")

#     @staticmethod
#     def greet():
#         print("************Hello there welcome to the best calculator of the world**********")

# a = Calculator(4)
# a.square()
# a.squareRoot()
# a.cube()
# a.greet()




# <----------------pr 5------------------------>
# Write a class train which has methods to book a ticket, get status(no of seats) and get fare information of trains running under Indian Railways.
# <-------------------------------------------->

# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print("*******************")
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train are {self.seats}")
#         print("*******************")

#     def fareInfo(self):
#         print(f"The price of the ticket is : Rs.{self.fare}")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"Your ticket has been booked! Your seats number is {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("Sorry this train is full kindly try in tatkal")

#     def cancleTicket(self, seatnum):
#         self.seatnum = seatnum
#         seatnum = int(input("Which seat number you want to cancle : "))
#         list = [1,2,3,4,5,6,7,8,9,10]
#         list.append(seatnum)
#         self.seats += 1

# intercity = Train("Intercity Express: 14015", 90, 20)
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.cancleTicket(input)
# intercity.getStatus()




# <----------------pr 6------------------------>
# Can you change the self parameter inside a class to something else(say'harry'). Try changing self to 'slf' or 'harry' and see the effects.
# <-------------------------------------------->

# class Sample:
#     def __init__(slf, name):
#         slf.name = name

# obj = Sample("Harry")
# print(obj.name)