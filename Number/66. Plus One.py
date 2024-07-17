class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total=0
        res=[]
        for i in digits:
            # print(digits[i])
            total=total*10+i
        # print(total)

        total+=1
        total=str(total)

        for i in total:
            res.append(int(i))
        # print(res)

        return res



        