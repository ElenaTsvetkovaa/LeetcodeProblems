from typing import List


def contains_duplicates(nums: List):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True

        hashset.add(n)
    return False

def contains_duplicates_sorted(nums: List):

    sorted_nums = sorted(nums)

    for i in range(0, len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i+1]:
            return True

    return False

nums = [1,5,2,3]
print(contains_duplicates_sorted(nums))
