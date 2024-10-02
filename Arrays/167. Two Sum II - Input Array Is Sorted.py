class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in numbers:
        #     for j in range(i+1, len(numbers), 1):
        #         print(i,j)
        l_count=0
        l=numbers[0]
        r_count=(len(numbers)-1)
        r=numbers[r_count]
        # print(l,r)
        res=[]
        while (l+r)!=target:
            if l+r>target:
                r_count-=1
                r=numbers[r_count]
            elif l+r<target:
                l_count+=1
                l=numbers[l_count]
        res.append(l_count+1)
        res.append(r_count+1)
        # print(res)
        return res
