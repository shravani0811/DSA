# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=head
        # nex=head.next
        while a and a.next:
            # print(head.val)
            if a.val==a.next.val:
                a.next=a.next.next
                continue
                # print(head.val)
            a=a.next
            # if head.next:
            #     nex=head.next
        # print(head)
        return head

        