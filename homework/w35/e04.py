from random import randint

def printSum (a: int, b: int) -> None:
    print(f"{a} + {b} = {a + b}")

a = randint(0, 10)
b = randint(0, 10)

printSum(a, b)
