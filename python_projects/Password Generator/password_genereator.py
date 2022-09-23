from logging import exception
import string
import random

if __name__ == "__main__":
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    plen = int(input("Enter Password Length : "))

    print("Your Password is : ",end="")
    genratedPassword = ("".join(random.sample(s,plen)))
    print(genratedPassword)

    password = input("Enter a Genrated Password : ")

    if password == genratedPassword:
        print("You have a Access This Application.")
    else:
        print("Enter a Valid Password!")
