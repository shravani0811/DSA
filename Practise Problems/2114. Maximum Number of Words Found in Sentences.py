class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for i in sentences:
            t=i.split()
            if len(t)>max:
                max=len(t)
        return max
        