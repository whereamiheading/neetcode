class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2: return []

        from collections import Counter
        nums_dict = Counter(nums)
        output = []
        for key, value in nums_dict.items():
            if value > 1: 
                output.append(key)
        return output