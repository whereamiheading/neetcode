class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        from collections import Counter
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)

        for num in nums1_dict:
            if num in nums2_dict:
                output.append(num)
        return output