from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    m_pointer = m - 1
    n_pointer = n - 1
    curr_p = m + n - 1
    for i in range(n-1, -1, -1):

        if nums2[n_pointer] > nums1[m_pointer]:
            nums1[curr_p] = nums2[n_pointer]
            n_pointer -= 1
        elif nums2[n_pointer] < nums1[m_pointer]:
            nums1[curr_p] = nums1[m_pointer]
            m_pointer -= 1
        curr_p -= 1
    return nums1
# 1,2,3,0,0,6
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))