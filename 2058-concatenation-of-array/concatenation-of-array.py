class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        ans = []
        count = 0

        while count<2:
            for num in nums:
                ans.append(num)
            count += 1 
        return ans
        