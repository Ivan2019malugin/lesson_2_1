list1 = [2, 7, 5, 6, 9, 15]
new_list = []
list_itog = len(list1)
for i in range(list_itog):
    if list1[i] % 2 == 0:
        new_list.append(list1[i] / 4)
    else: new_list.append(list1[i] * 2)
print(new_list)
