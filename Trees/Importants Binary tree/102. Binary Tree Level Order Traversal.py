# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                # print(i)
                current=q.popleft()
                if current:
                    # print(current.val)
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            if level:
                res.append(level)
        # print(res)
        return res
        