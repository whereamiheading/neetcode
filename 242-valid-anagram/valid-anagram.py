class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False

        t_dict, s_dict = {}, {}
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1

        # for key in t:
        #     if t_dict[key] != s_dict.get(key,0):
        #         return False
        
        # return True
        return t_dict == s_dict


