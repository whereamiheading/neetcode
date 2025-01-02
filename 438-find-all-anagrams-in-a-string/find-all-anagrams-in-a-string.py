class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        output = []
        if len(p) > len(s):
            return output
        p_count = Counter(p)
        window = Counter()
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1
            if right - left + 1 > len(p):
                if window[s[left]] == 1:
                    del window[s[left]]
                else:
                    window[s[left]] -= 1
                left += 1
            if window == p_count:
                output.append(left)
        return output