from typing import List


def remove_element(nums: List[int], val: int) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


# 2, 2, 1, 1        2
nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(nums, val))

