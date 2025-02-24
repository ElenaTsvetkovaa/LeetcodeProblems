
class Solution:
    def maximum_wealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Option 1
        # max_wealth = 0
        # for row in range(len(accounts)):
        #     curr_sum = sum(accounts[row])
        #
        #     if curr_sum > max_wealth:
        #         max_wealth = curr_sum
        # return max_wealth

        # Option 2
        return max(map(sum, accounts))


m = [[1,5], [7,3], [3,5]]
s = Solution()
print(s.maximum_wealth(m))
