"""
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(word: str) -> bool:
    length = len(word)
    for el in range(length // 2):
        if word[el] != word[length - 1 - el]:
            return False
    return True


mx = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        number = i * j
        checker = palindrome(str(number))
        if checker:
            if number > mx:
                mx = number
print(mx)
