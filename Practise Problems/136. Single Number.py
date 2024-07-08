class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res={}
        for i in nums:
            if i not in res:
                res[i]=1
            else:
                res[i]+=1
        # print(res)

        for key, value in res.items():
            if value==1:
                return key

        