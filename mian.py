import random


a = random.randint(1, 100)

while True:
    print(a)
    num = int(input("Chose number:"))
    if a == num:
        print("You win!!!")
        break
    elif a < num:
        print("Много")
    elif a > num:
        print("Мало")

print("Exit")