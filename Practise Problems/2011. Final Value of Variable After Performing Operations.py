class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res=0
        # comp=['--X':-1,'X--':-1,'++X':+1,'X++':+1]
        # for key,val in operations.items():
        for i in operations:
            if i=="--X" or i=="X--":
                res-=1
                # print(res)
            else:
                res+=1
                # print(res)
        return res
