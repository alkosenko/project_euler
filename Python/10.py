"""
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.
"""

array = [int(num) for num in range(2000000)]
array[1] = 0

sum_of_prime = 0
for el in range(len(array)):
	if array[el] != 0:
		for not_prime in range(array[el]*2, len(array), array[el]):
			array[not_prime] = 0
		else:
			sum_of_prime += array[el]
print(sum_of_prime)
