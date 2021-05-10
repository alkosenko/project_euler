"""
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
"""

number = 600851475143
div_max = 0
for divisor in range(2, int(number ** 0.5)):
    while number % divisor == 0:
        number //= divisor
        div_max = divisor
    if number == 1:
        break
print(div_max)
