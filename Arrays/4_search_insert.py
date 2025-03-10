from typing import List


def search_insert(nums: List[int], target: int) -> int:

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (right + left) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        elif  mid_el > target:
            right = mid_idx - 1

        else:
            left = mid_idx + 1
    return left

nums = [1,3,5,6]
target = 5
print(search_insert(nums, target))
