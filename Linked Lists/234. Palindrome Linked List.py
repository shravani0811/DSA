# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res=[]
        rev=[]
        while head:
            res.append(head.val)
            head=head.next
        # print(res)

        # for i in range(len(res)-1, -1,-1):
        #     rev.append(res[i])
        # # print(rev)

        # for i in range(len(res)):
        #     if res[i]!=rev[i]:
        #         return False
        # return True
        l,r=0, len(res)-1
        # print(l,r)
        while l<=r:
            if res[l]!=res[r]:
                return False
            l+=1
            r-=1
        return True
        