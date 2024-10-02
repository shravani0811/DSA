class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        check={')':'(',']':'[','}':'{'}
        for i in s:
            if i in check and stack:
                # print("top element", stack[-1], "i",check[i])
                if stack[-1] ==check[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
            # print(stack)
        if len(stack)==0:
            return True
        return False

        