class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=len(needle)
        for i in range(len(haystack)-l+1):
            if needle==haystack[i:i+l]:
                # print(haystack[i:i+l])
                return i
        return -1
        