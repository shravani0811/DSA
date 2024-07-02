class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(nums)
        # # n=[1,9,2,3,4]
        nums.sort()
        # print(nums)
        start=0
        counter=0
        # start=int(nums[0])
        for i in nums:
            if i!=start:
                s=start
                counter=1
                return s
            start+=1
        if counter==0:
            return len(nums)