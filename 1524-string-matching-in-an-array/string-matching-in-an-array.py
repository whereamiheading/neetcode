class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        
        for i, word in enumerate(words):
            if i == len(words)-1:
                if word in ('.'.join(words[:i])):
                    output.append(word)
            else:
                if word in '.'.join(words[:i] + words[i+1:]):
                    output.append(word)
        return output

        