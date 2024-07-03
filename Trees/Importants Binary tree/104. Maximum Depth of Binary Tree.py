# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        q=collections.deque()
        q.append(root)
        if not root:
            return 0
        level=1
        while q:
            l=len(q)
            
            for i in range(l):
                # print(i)
                current=q.popleft()
                if current:
                    # print(current.val)
                    # print("level",level)
                    res.append(level)
                    
                    q.append(current.left)
                    q.append(current.right)
            level+=1
        # print(res)
            # print("level",level)
        # print(level)   # res.append(level)
        return max(res)


        