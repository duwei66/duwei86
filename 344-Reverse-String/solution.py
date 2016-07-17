class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = str(s)
        j = len(s)-1
        u = ''
        while (j>=0):
            u += s[j]
            j -= 1
        return u