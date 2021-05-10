"""
    By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
"""

array = list(range(0, 1000000))
array[1] = 0
count_prime_numbers = 0

for el in range(len(array)):
    if array[el] != 0:
        for j in range(array[el] * 2, len(array), array[el]):
            array[j] = 0
        else:
            count_prime_numbers += 1
            if count_prime_numbers == 10001:
                print(array[el])
                break
