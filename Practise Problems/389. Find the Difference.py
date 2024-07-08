class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        # """
        # for i in t:
        #     # print(i)
        #     if i not in s:
        #         return i
        #         # print(i)
        # print(t-s)
        s_sub={}
        t_sub={}
        for i in s:
            if i not in s_sub:
                s_sub[i]=1
            else:
                s_sub[i]+=1

        for i in t:
            if i not in t_sub:
                t_sub[i]=1
            else:
                t_sub[i]+=1

        for key, value in t_sub.items():
            if key not in s_sub:
                return key
            elif value !=s_sub[key]:
                return key
        print(s_sub)
        print(t_sub)
            

        
        