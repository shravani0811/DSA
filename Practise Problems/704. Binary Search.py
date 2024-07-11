class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower=0
        upper=len(nums)-1
    
        while lower<=upper:
            # print("uppper", target,"lower",lower)
            mid=((lower+upper)//2)
            if target ==nums[mid]:
                # print("target", target,"mid",nums[mid])
                return mid
            elif target>nums[mid]:
                lower=mid+1
            elif target<nums[mid]:
                upper=mid-1
        return -1


        # print(mid)
        # return 0
        