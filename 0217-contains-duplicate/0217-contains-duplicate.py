class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_check = set()

        for num in nums:
            if num in set_check:
                return True
            else:
                set_check.add(num)
        return False