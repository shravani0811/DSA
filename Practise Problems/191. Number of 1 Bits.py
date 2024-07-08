class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=bin(n)
        num=num.replace("0b","")
        one=0
        num=str(num)
        for i in num:
            print(i)
            if i=="1":
                # print("yess")
                one+=1
        return one
        