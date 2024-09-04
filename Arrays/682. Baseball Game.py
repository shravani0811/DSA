class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res=[]
        for i in operations:
            # print(i)
            if i=="C":
                res.pop()
            elif i=="D":
                l=res[-1]
                # print(l)
                res.append(2*int(l))
            elif i=="+":
                res.append(res[-1]+res[-2])
            else:
                res.append(int(i))
        total=0
        for i in res:
            total+=i

        # print(total)
        return total