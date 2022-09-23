# <----------------pr 1------------------------>
# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'
# <-------------------------------------------->

# with open("text_files/poems.txt") as f:
#     content = f.read()

# if 'twinkle' in content.lower():
#     print("Twinkle is present in text files.")
# else:
#     print("Twinkle is not present in text files.")




# <----------------pr 2------------------------>
# The Game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains the previous hi-score. you need to write a program to update the hi-score whenever game() breaks the hi-score.
# <-------------------------------------------->

# score = int(input("Enter you highscore : "))
# with open("text_files/hiscore.txt") as f:
#      hiscore = f.read()

# with open("text_files/hiscore.txt" , 'w') as f:
#         if hiscore == "":
#             f.write(str(score))
#         elif int(hiscore)<score:
#             f.write(str(score))

# with open("text_files/hiscore.txt") as f:
#      highscore = f.read()

# print(f"Your High Score is {highscore}")




# <----------------pr 3------------------------>
# Write a program to generate multiplication tables from 2 to 20 and write it to the diffrent files. place these files in a folder for a 13 years old.
# <-------------------------------------------->

# for i in range(2,21):
#     with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j} = {i*j}")
#         if j != 10:
#             f.write('\n')




# <----------------pr 4------------------------>
# A file contains a word 'donkey' multiple times. you need to write a program which replaces this word with  ###### by updating the same file.
# <-------------------------------------------->


# with open("text_files/replace word.txt") as f:
#     content = f.read()
#     if 'donkey' in content:
#        content = content.replace("donkey" , "#$%@*%^#")

# with open("text_files/replace word.txt",'w') as f:
#     f.write(content)




# <----------------pr 5------------------------>
# repeat program 4 for a list of such words to be censored.
# <-------------------------------------------->

# list = ['donkey', 'ugly', 'motu']

# with open("text_files/replace_word.txt") as f:
#     content = f.read()

# for word in list:
#         content = content.replace(word, "#$%@*%^#")
#         with open("text_files/replace_word.txt","w") as f:
#             f.write(content)




# <----------------pr 6------------------------>
# Write a program to prime a log file and find out whether it contains 'python'.
# <-------------------------------------------->

# with open("text_files/log.txt") as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Python is present in log file.")
# else:
#     print("Python is not present in log file.")




# <----------------pr 7------------------------>
# Write a program to find out the line number where python is present from que. 6.
# <-------------------------------------------->

# content = True
# i = 1
# with open("text_files/log.txt") as f:
#     while content:
#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"Yes Python is present on line number {i}")
#         i+=1




# <----------------pr 8------------------------>
# Write a program to make a copy of a text file "this.txt".
# <-------------------------------------------->

# with open("text_files/this.txt") as f:
#     content = f.read()

# with open("text_files/copy.txt" , "w") as f:
#     f.write(content)




# <----------------pr 9------------------------>
# Write a program to find out whether a file is identical & matches the content of another file.
# <-------------------------------------------->

# file1 = ("text_files/this.txt")
# file2 = ("text_files/copy.txt")

# with open(file1) as f:
#     f1 = f.read()
# with open(file2) as f:
#     f2 = f.read()

# if f1==f2:
#     print("This is a identical files.")
# else:
#     print("This is not identical files.")




# <----------------pr 10------------------------>
# Write a program to wipe out the contents of a file using python.
# <-------------------------------------------->

# with open("text_files/another.txt") as f:
#     content = f.read()

# with open("text_files/another.txt", "w") as f:
#     content = f.write("")



# <----------------pr 11------------------------>
# Write a python program to rename a file to "renamed_by_python.txt"
# <-------------------------------------------->

# import os
# oldfile = "text_files/sample2.txt"
# newfile = "text_files/removed_by_python.txt"
# with open(oldfile) as f:
#     content = f.read()

# with open(newfile,"w") as f:
#     f.write(content)

# os.remove(oldfile)