class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
##### NOSTALIA PALIDROME CHECK FROM SCHOOL LOLL #########

        # ld=0
        # nums=x
        # res=0
        # while nums!=0:
        #     ld=nums%10
        #     nums=nums/10
        #     res=res*10+ld
        # print(res)

        # return res
        neg=0
        res=""
        new_x=""
        if x<0:
            neg=neg+1
        
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31
        # new_x=[i for i in range(len(x),1,-1)]
        x=str(abs(x))
        # print(x)
        for i in range(len(x)-1,-1,-1):
            new_x+=x[i]

        if neg==1:
                res+="-"

        for i in new_x:
            res+=str(i)

        res = int(res)

        if res < MIN_INT or res > MAX_INT:
            return 0

        # print(int(res))
        return res


        