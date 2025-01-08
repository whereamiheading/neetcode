import uuid
class Codec:
    def __init__(self):
        self.long_tiny = {}
        self.tiny_long = {}
        self.base = 'http://tinyurl.com/'

    def get_key(self):
        return str(uuid.uuid4())[:6]

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_tiny:
            return self.long_tiny[longUrl]
        
        key = self.get_key()
        
        while self.base + key in self.tiny_long:
            key = self.get_key()
        
        tiny_url = self.base + key
        self.long_tiny[longUrl] = tiny_url
        self.tiny_long[tiny_url] = longUrl
        return tiny_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.tiny_long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))