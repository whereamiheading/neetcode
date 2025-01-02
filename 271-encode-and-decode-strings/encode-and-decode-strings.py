class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + ":" + s
        return ''.join(encoded)



    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        decoded = []
        i = 0 
        while i < len(s):
            j = s.find(":", i)
            length = int(s[i:j])
            i = j+1
            decoded.append(s[i:i+length])
            i +=length
        
        return decoded

        return decoded
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))