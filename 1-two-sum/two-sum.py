class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx_dict = {}
        for idx, num in enumerate(nums):
            res = target - num
            if res in idx_dict:
                return [idx_dict[res],idx]
            else:
                idx_dict[num] = idx