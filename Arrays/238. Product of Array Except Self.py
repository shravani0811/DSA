class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        zeros=0
        result=[0]*len(nums)
        print(result)
        for i in nums:
            if i!=0:
                product*=i
            else:
                zeros+=1
        print(product)
        res= [i for i in range(len(nums)) if nums[i]==0]
        print(res)
        if zeros>1:
            return result

        elif len(res)>0:
            for i in res:
                result[i]=product
        #         result[i]=product
        #         break
        else:
            for i in range(len(nums)):
                result[i]=product/nums[i]
        #     else:
        #         result[i]=product/nums[i]
        return result