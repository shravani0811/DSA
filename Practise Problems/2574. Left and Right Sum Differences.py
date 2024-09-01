class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum=[]
        rightsum=[]
        right=[]
        n=len(nums)
        res=[]
        total=0
        leftsum.append(total)
        rightsum.append(total)
        

        for i in range(n-1):
            total+=nums[i]
            leftsum.append(total)
        # print(leftsum)

        total=0

        for i in range(n-1,0,-1):
            total+=nums[i]
            rightsum.append(total)
        # print(rightsum)

        for i in range(n-1,-1,-1):
            right.append(rightsum[i])
        # print(right)

        for i in range(n):
            res.append(abs(leftsum[i]-right[i]))
        return res

            

        