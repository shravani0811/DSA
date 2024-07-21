class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if x==0:
            return 0
        if n==0:
            return 1
        total=1
        for i in range(abs(n)):
            total*=x
        if n<0:
            total=1/total
        # print(total)
        return total
            
        