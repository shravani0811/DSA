class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        t=s.split(" ")
        result=""
        print(t)
        reversed=t[::-1]
        for i in reversed:
            if i!="":
                result+=i + " "
        # print(result)
        return result.strip()


        