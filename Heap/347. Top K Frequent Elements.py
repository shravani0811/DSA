class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if k==len(nums):
        #     return nums
        if k>len(nums):
            return []
        res={}
        output=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in res:
                res[i]=1
            else:
                res[i]+=1

        for i,j in res.items():
            output[j].append(i)
        final=[]
        for i in range(len(output)-1,0,-1):
            for j in output[i]:
                final.append(j)
                # print(i)
                if len(final)==k:
                    return final
                    # print(final)
        # for i in res:
        #     if i <k:
        #         output.append(i)
        # print(output)
        # print(output)
        # return output