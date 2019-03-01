import math
sqad_list = [2, -5, 8, 9, -25, 25, 4]
itog_list = []
for element in sqad_list:
    if (element > 0) and (int(math.sqrt(element)) == math.sqrt(element)):
        itog_list.append(int(math.sqrt(element)))
print(itog_list)

