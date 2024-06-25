class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_list=['a','e','i','o','u','A','E','I','O','U']
        vowels=[]
        result=""
        for i in s:
            if i in vowel_list: 
                vowels.append(i)
        # print(vowels)
        val=len(vowels)-1
        # print(val)
        for i in s:
            if i in vowel_list: 
                result+=vowels[val]
                val-=1
                # print(val)
            else:
                result+=i
        return result
        