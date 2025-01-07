from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = Counter(s)
        for idx, letter in enumerate(s):
            if dt[letter] == 1:
                return idx
        return -1   