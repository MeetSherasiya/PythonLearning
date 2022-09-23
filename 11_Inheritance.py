# <----------------pr 1------------------------>
# Create a class C2d vector and use it to create another class representing a 3-d vector.
# <-------------------------------------------->

# class C2dVec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(C2dVec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

# v2d = C2dVec(1, 3)
# v3d = C3dVec(1, 9, 7)
# print(v2d)
# print(v3d)




# <----------------pr 2------------------------>
# Create a class pets from a class animals and further create class dog from pets. Add a method bark to class Dog.
# <-------------------------------------------->

# class aminals:
#     animalType = "Mammal"

# class pets:
#     color = "White"

# class Dog:
#     @staticmethod
#     def bark():
#         print("Bow bow!")

# d = Dog()
# d.bark()




# <----------------pr 3------------------------>
# Create a class employee and add salary and increment properties to it. write a method salaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.
# <-------------------------------------------->

# class Employee:
#     salary = 1000
#     increment = 1.5

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * self.increment

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, sai):
#         self.increment = sai/self.salary

# e = Employee()
# print(e.salary)
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 4500
# print(e.increment)





# <----------------pr 4------------------------>
# Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.
# <-------------------------------------------->

# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imagnary = i

#     def __add__(self, c):
#         return Complex(self.real + c.real , self.imagnary + c.imagnary)

#     def __mul__(self, c):
#         mulReal = self.real*c.real - self.imagnary*c.imagnary
#         mulImg = self.real*c.imagnary + self.imagnary*c.real
#         return Complex(mulReal, mulImg)

#     def __str__(self):
#         if self.imagnary<0:
#             return f"{self.real} - {-self.imagnary}i"
#         else:
#             return f"{self.real} + {self.imagnary}i"

# c1 = Complex(1, 4)
# c2 = Complex(4, 3)
# print(c1 + c2)
# print(c1 * c2)




# <----------------pr 5------------------------>
# Write a class vector representing a vetor of n dimension overload the + and * operator which calculates the sum and the dot product of them.
# <-------------------------------------------->

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index += 1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# print(v1+v2)
# print(v1*v2)





# <----------------pr 6------------------------>
# Write __str__() method to print the vector as follows: 7i + 8j + 10k assume vector of dimension 3 for this problem.
# <-------------------------------------------->

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

# v1 = Vector([1, 4, 6])
# print(v1)



# <----------------pr 7------------------------>
# Override the __len__() method on vector of problem 5 to display the dimension of the vector.
# <-------------------------------------------->

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index += 1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

#     def __len__(self):
#         return len(self.vec)

# v1 = Vector([1, 4, 6, 9, 8, 7])
# v2 = Vector([1, 6, 9])
# print(len(v1))
# print(len(v2))




# <----------------pr 8------------------------>
# Length is same print the vector else show an error message.
# <-------------------------------------------->

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index += 1
#         return str1[:-1]

#     def __add__(self, vec2):
#         if len(self.vec)!= len(vec2.vec):
#             print("Addition of length of vector are not equal.")
#         else:
#             newList = []
#             for i in range(len(self.vec)):
#                 newList.append(self.vec[i] + vec2.vec[i])
#             return Vector(newList)

#     def __mul__(self, vec2):
#         if len(self.vec)!= len(vec2.vec):
#             print("Multiplication of length of vector are not equal.")
#         else:
#             sum = 0
#             for i in range(len(self.vec)):
#                 sum += self.vec[i] * vec2.vec[i]
#             return sum

#     def __len__(self):
#         return len(self.vec)

# v1 = Vector([1, 4])
# v2 = Vector([1, 6, 9])
# print(v1+v2)
# print(v1*v2)