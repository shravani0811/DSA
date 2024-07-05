##### 11:57 #####

class Solution(object):
    def findDuplicate(self, nums):
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
        for key, value in res.items():
            if value>=2:
                return key