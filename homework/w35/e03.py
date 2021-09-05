from random import randint

a = randint(0, 100)
b = randint(0, 100)

if a > b:
    print("a is bigger")
elif b > a:
    print("b is bigger")
else:
    print("a and b are equal")

