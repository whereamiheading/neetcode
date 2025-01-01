class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import Counter
        freq = Counter(chars)
        output = 0
        for word in words:
            word_count = Counter(word)
            if all(word_count[ch] <= freq[ch] for ch in word):
                output += len(word)
        return output