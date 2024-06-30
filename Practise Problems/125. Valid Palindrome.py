class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        val=""
        s=s.lower()
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) :
                val+=i
        # print(val)
        i=0
        j=len(val)-1
        while i<=j:
            if val[i]!=val[j]:
                return False
            i+=1
            j-=1
        return True
        

                

        