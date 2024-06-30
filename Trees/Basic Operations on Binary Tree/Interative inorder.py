### I HATE THIS APPROACH BUT COOL ####


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        stack=[]
        curr=root

        while curr or stack: # while they are not null
            while curr: #while their exists a current value
                stack.append(curr)
                curr=curr.left #keep moving to the left most side of the tree
            curr=stack.pop
            res.append(curr.val)#append the left most to the result array
            curr=curr.right # go to the right node of the root
        return res
        