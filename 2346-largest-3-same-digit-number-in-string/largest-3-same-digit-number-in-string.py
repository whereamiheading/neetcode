class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        output = ""
        left, right = 0, 0
        max_output = ""

        for left in range(0, len(num)-2):
            if len(set(num[left:left+3])) == 1:
                max_output = max(num[left:left+3], max_output)
            left += 1
        return str(max_output)
        









        return output