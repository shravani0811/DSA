class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        u1=set()
        u2=set()
        for i in nums1:
            if (i not in nums2):
                u1.add(i)
        for i in nums2:
            if (i not in nums1 ):
                u2.add(i)

        return(u1, u2)


##### BRUTE FORCE #########

        # u1=[]
        # u2=[]
        # for i in nums1:
        #     if (i in nums2 ) or (i in u1):
        #         continue
        #     else:
        #         u1.append(i)
        # for i in nums2:
        #     if (i in nums1 ) or (i in u2):
        #         continue
        #     else:
        #         u2.append(i)

        # return(u1, u2)
        