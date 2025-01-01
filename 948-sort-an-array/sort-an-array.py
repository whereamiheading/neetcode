class Solution(object):
    def merge_sort_helper(self, l1, l2):
        sorted = []
        while l1 and l2:
            if l1[0] <= l2[0]:
                sorted.append(l1.pop(0))
            else:
                sorted.append(l2.pop(0))
        sorted.extend(l1 if l1 else l2)
        return sorted
                        


    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) <=1: return nums
        n = len(nums)    
        left = self.sortArray(nums[:n/2])
        right = self.sortArray(nums[n/2:])

        return self.merge_sort_helper(left, right)