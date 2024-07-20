class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        res=[0]*(n+1)
        offset=1

        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            res[i]=1+res[i-offset]
        return res




    #     res=[]
    #     nums=[]
    #     check={0:0,1:1,2:1,3:2}
    #     for i in range(n+1):
    #         # curr=bin(i).replace('0b',"")
    #         # res.append(curr)
    #         nums.append(i)
    #     # print(18/4)
    #     for i in nums:
    #         plus=i/4
    #         val=i%4
    #         if val!=0:
    #             res.append(plus+check[val])
    #         else:
                
    # return res

        