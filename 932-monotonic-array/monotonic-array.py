class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[-1] < nums[0]:
            nums = nums[::-1]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True