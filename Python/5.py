"""
    2520 is the smallest number that can be divided
    by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is
    evenly divisible by all of the numbers from 1 to 20?
"""


def gdc(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


def lcd(a: int, b: int) -> int:
    return (a * b) // gdc(a, b)


number = 1
for num in range(2, 21):
    number = lcd(number, num)
print(number)
