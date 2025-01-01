class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        largest = ""
    
        # Iterate through the string
        for i in range(len(num) - 2):
            # Check if three consecutive digits are the same
            if num[i] == num[i + 1] == num[i + 2]:
                # Get the current 3-digit substring
                current = num[i:i + 3]
                # Update largest if current is greater
                if current > largest:
                    largest = current
        
        return largest