fruits = ["яблоко", "банан", "киви", "арбуз"]
length = len(fruits)
for i in range(length):
    print(F"{str(i + 1)}. {(fruits[i]).rjust(10)}");