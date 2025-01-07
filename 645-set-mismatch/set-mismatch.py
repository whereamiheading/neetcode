class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        freq = Counter(nums)
        output = []
        for k,v in freq.items(): 
            if v>1: output.append(k)
        output.append(sum([num for num in range(1, len(nums)+1)]) - sum(freq.keys()))

        return output
        