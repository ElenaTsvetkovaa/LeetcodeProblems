
class Solution:
    def running_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
            Time complexity is On because we need to loop through all numbers.
            Start from the second num because the first is never changing - we don't 
            sum it up with the previous one.
            Use indexing to access nums faster.
        """

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums

# Test cases
nums = [1, 2, 3, 4]  # expected [1, 3, 6, 10]

