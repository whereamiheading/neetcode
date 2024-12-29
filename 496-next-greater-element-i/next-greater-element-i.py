class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # output = []

        # for i, num in enumerate(nums1):
        #     idx = nums2.index(num)
        #     # print(nums2[idx], idx)
        #     next_greater = -1
        #     for j in range(idx+1, len(nums2)):
        #         if nums2[j] > num:
        #             next_greater = nums2[j]
        #             break
        #     output.append(next_greater)
        # return output

        stack = []
        next_greater = {}

        for num in reversed(nums2):
            while stack and stack[-1]<= num:
                stack.pop()
            
            next_greater[num] = stack[-1] if stack else -1

            stack.append(num)
        
        return [next_greater[num] for num in nums1]
