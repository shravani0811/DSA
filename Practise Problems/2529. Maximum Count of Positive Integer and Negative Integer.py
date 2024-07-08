class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res={"pos":0,"neg":0}
        for i in nums:
            if i<0:
                res["neg"]+=1
            elif i>0:
                res["pos"]+=1
        return (res[(max(res))])
        