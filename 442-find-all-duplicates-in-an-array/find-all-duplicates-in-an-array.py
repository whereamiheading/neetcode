class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2: return []

        output = []

        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                output.append(abs(n))
            else:
                nums[index] = -nums[index]
        return output
