class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,1,1] : if 4th 1 is to come in, we have to pair with existing 3 in the room.Hence, count += freq[num]
        """
        freq = {}
        count = 0
        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return count