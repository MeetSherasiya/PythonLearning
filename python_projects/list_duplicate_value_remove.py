lst = [1,6,2,5,2,1,5,8,4,9]

# for i in lst:
#     idx = lst.index(i)

# for item in lst[:]:
#     index = lst.index(item) + 1
#     while index < len(lst):
#         if lst[index] == item:
#             del lst[index]
#         index += 1


#******************* Second Method ***********************

i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[j] == lst[i]:
            del lst[j]
        else:
            j += 1
    i += 1

print(lst)