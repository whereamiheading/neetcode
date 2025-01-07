class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            left_empty, right_empty = False, False
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i-1] == 0:
                    left_empty = True
                if i == len(flowerbed)-1 or flowerbed[i+1] == 0:
                    right_empty = True
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
        