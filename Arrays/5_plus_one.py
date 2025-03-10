from typing import List

def plus_one(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    digits.insert(0, 1)
    return digits

def recursive_plus_one(digits):
    if not digits:
        return [1]

    if digits[-1] < 9:
        digits[-1] += 1
        return digits

    digits[-1] = 0
    return recursive_plus_one(digits[:-1]) + [0]



digits = [1,9,9]  # [1, 0]
print(recursive_plus_one(digits))
