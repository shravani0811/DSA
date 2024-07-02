import math
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
######       this cant be a easy problem or am i dumb ???!!!       ######

        f=[0]+flowerbed+[0]
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                if n>0:
                    f[i]=1
                    n-=1
        if n<=0:
            return True
        else:
            return False




        # map={}
        # for i in flowerbed:
        #     if i not in map:
        #         map[i]=1
        #     else:
        #         map[i]+=1
        # if n<=(map[0]-2):
        #     # print("True")
        #     return True
        # else:
        #     # print("False")
        #     return False
        
        # possible= int(math.ceil(float(len(flowerbed))/2))
        # # print("lenth:", len(flowerbed))
        # print("possible:",possible)
        # if len(flowerbed)%2!=0:
        #     if flowerbed[0]==0 and flowerbed[len(flowerbed)-1]==0:
        #         possible= possible-1
        # print("odd/even", len(flowerbed)%2)
        # print("possible:",possible)
        # print("last",flowerbed[len(flowerbed)-1])
        # planted=0
        # for i in flowerbed:
        #     if i==1:
        #         planted+=1
        # available =possible-planted
        # if n<=available:
        #     return True
        # return False
        # print(available)