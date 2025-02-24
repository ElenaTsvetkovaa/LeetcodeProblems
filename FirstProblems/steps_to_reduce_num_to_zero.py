class Solution(object):
    def number_of_steps(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            counter += 1

        return counter

print(Solution().number_of_steps(14))