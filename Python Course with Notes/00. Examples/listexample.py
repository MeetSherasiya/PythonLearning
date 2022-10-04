lst = [1,4,1,5,2,6,1,6,3,2,7,4,2,7,5,2]
list = []

for i in lst:
    if i not in list:
        list.append(i)

lst = list
print(lst)