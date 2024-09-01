class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[0]*(2*n)
        print(res)
        for i in range(n):
            res[i],res[(i+n)]=nums[i], nums[i]
        return res
