class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # word1=list(word1)
        # word2=list(word2)
        # val=abs(len(word1)-len(word2))
        # if len(word1)>len(word2):
        #     word2.append("$"*val)
        # else:
        #     word1.append("$"*val)
        # # for i in r\

        # if len(word1)>len(word2):
        #     val=len(word2)
        # else:
        #     val=len(word1)
        # # # merged=
        # while 
        # # print (len(word2))
        # return ""

        word=""
        one=word1[-1]
        print(one, word1)

        while word1 and word2:
            one=word1[0]
            two=word2[0]
            word+=one+two
            word1=word1[1:]
            word2=word2[1:]
        word+=word1+word2
        return word

