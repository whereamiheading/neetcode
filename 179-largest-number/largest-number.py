class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def compare(x, y):
            if x + y > y + x:
                return -1  
            elif x + y < y + x:
                return 1   
            else:
                return 0
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return result if result[0] != '0' else '0'