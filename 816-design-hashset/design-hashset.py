class MyHashSet(object):

    def __init__(self):
        self.capacity = 10000
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key):
        return hash(key) % self.capacity
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        if key not in bucket: 
            bucket.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """        
        index = self._hash(key)
        bucket = self.buckets[index]

        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        flag_exists = key in bucket
        return flag_exists


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)