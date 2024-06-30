class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        res={}
        l=len(arr)
        # if 4 in res.values():
            # print("yes")
        
        for i in arr:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        print(res)

        counting={}
        for i in res.values():
            if i in counting:
                return False
            counting[i]=1
        return True
                
        
        # for i in range(l):
        #     count=1
        #     if i not in res:
        #         for j in range(i+1,l,1):
        #             print("i",arr[i],"j",arr[j])
        #             if arr[i]==arr[j]:
        #                 count+=1
        #                 # print("count",count)
        #     if count not in res.values():
        #             # return False
        #         res[arr[i]]=count
        # print(res)

        



        