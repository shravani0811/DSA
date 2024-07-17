class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        res=s.split(" ")
        print(res)
        return (len(res[len(res)-1]))