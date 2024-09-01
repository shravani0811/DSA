class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res=[]
        # first=[]
        # last
        l=len(nums)
        for i in range(l/2):
            res.append(nums[i])
            res.append(nums[i+n])
        # print(res)
        return res
        