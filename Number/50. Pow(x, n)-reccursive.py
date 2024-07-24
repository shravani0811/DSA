class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # if x==0:
        #     return 0
        # if n==0:
        #     return 1
        # total=1
        # odd=0
        # diff=0
        # if n%2 !=0:
        #     odd+=1
        # multiplier=n//2
        # diff=n-(2*multiplier)
        # total=(x**multiplier)*(x**multiplier)
        # if odd==1:
        #     total=total*2
        # if diff>0:
        #     total+=
        # print(total)
        # return 0.0

        def doit(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=doit(x,n//2)
            res=res*res
            return x*res if n%2 else res
        res=doit(x,abs(n))
        return res if n>=0 else 1/res
    
    #yess


        # for i in range(abs(n)):
        #     total*=x
        # if n<0:
        #     total=1/total
        # # print(total)
        # return total
            
        