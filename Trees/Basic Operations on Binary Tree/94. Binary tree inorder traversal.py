# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### RECURSIVE METHOD ###

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]

        def inorder(root):

            if not root:
                return

            inorder(root.left)

            res.append(root.val)

            inorder(root.right)

            # print(res)
        inorder(root)
        return res


        