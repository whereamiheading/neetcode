class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1 

        while left <=right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -=1 
            else:
                left +=1
        return left
    
            