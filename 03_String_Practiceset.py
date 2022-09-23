# <----------------pr 1------------------------>
# Write a python program to display a user entered name followed by Good Afternoon using input() function.
#<----------------------------------------------------->

# name = input("Enter your name\n")
# print("Good Afternoon," + name)


# <----------------pr 2------------------------>
# Write a program to fill in a letter templete given below with name and date. letter = ''' Dear <|NAME|>, you are Selected! <|DATE|>'''
#<----------------------------------------------------->

# letter='''Dear <|Name|>,
# You are selected!
# Date: <|DATE|>'''
# name = input("Enter Your Name\n")
# Date = input("Enter Date\n")
# letter = letter.replace("<|Name|>",name)
# letter = letter.replace("<|DATE|>",Date)
# print(letter)

# <----------------pr 3 & 4---------------------------->
# Write a program to detect double spaces in a string. replace the double spaces with single spaces.
#<----------------------------------------------------->

# st = "This is a string with double  spaces"

# doubleSpaces= st.find("  ")
# st = st.replace("  ","   ")
# print(doubleSpaces)
# print(st)




# <---------------pr 5----------------------->
# Write a program to format the following letter using escape sequence characters.
# Letter = "Dear Harry, This Python course is nice. Thanks!"
#<----------------------------------------------------->

# letter = "Dear Harry, This Python course is nice. Thanks!"
# print(letter)

# formatted_letter = "Dear Harry,\n\n\tThis Python course is nice.\n\nThanks!"
# print(formatted_letter)