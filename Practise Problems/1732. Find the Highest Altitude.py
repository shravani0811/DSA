class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[0]
        update=0
        for i in gain:
            update+=i
            res.append(update)
        # print(res)
        return (max(res))
        