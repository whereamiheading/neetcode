class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        c_w = {}
        w_c = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c in c_w:
                if c_w[c] != w:
                    return False
            else:
                c_w[c] = w

            if w in w_c:
                if w_c[w] != c:
                    return False
            else:
                w_c[w] = c
        return True
        