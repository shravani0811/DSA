class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums),1):
                if nums[i]==nums[j]:
                    return True
        return False
