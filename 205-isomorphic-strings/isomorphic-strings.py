class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_s_to_t = {}
        mapped_characters = set()

        for char_s, char_t in zip(s,t):
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_characters:
                    return False
                mapping_s_to_t[char_s] = char_t
                mapped_characters.add(char_t)
        return True


