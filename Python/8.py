"""
	The four adjacent digits in the 1000-digit number that have
	the greatest product are 9 × 9 × 8 × 9 = 5832.
	Find the thirteen adjacent digits in the 1000-digit number
	that have the greatest product. What is the value of this product?
"""


def product_string(number: str) -> int:
	result = 1
	for el in range(len(number)):
		result *= int(number[el])
	return result


word = ""
file = open("txt_files_for_problems/8.txt", "r", encoding="utf-8")
for line in file.readlines():
	word += line.replace("\n", "")

mx_product = 0
for char in range(0, len(word) - 13):
	product = product_string(word[char:char+13])
	mx_product = max(product, mx_product)
print(mx_product)
