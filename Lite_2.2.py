list1 = [1, 2, 3, 'A', 'B', 6, 7]
list2 = [6, 2, 'B', 'F']
for item in list2:
    if item in list1:
        list1.remove(item)
print("Решение 1: " f"{list1}")


# Решение 2
list1 = {'a', 'b', 'c', 'c', 'a', 'e'}
list2 = {'a', 'b', 'c', 'd'}
list3 = list1 - list2
print("Решение 2: " f"{list(list3)}")
