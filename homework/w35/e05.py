from random import randint
from functools import reduce
from typing import List

def count_correct_answers(count: int, q: List[int]) -> int:
    if q[0] * q[1] == q[2]:
        count += 1

    return count

qs = []

for _ in range(5):
    a = randint(0, 10)
    b = randint(0, 10)
    qs.append([a, b])

for i in range(len(qs)):
    [a, b] = qs[i]
    qs[i].append(int(input(f"{a} * {b} = ")))
    print()

for [a, b, c] in qs:
    if a * b == c:
        print(f"Correct :-) {a} * {b} = {a * b}")
    else:
        print(f"Wrong :-( Correct was: {a} * {b} = {a * b}")

answers_correct = reduce(count_correct_answers, qs, 0)

print(f"You got {answers_correct} questions right!")
