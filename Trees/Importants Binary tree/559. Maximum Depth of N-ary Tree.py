"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        res=[]
        q=collections.deque()
        q.append(root)
        if not root:
            return 0
        
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                # print(i)
                current=q.popleft()
                if current:
                    for i in current.children:
                        level.append(i.val)
                    # print(current.val)
                    # print("level",level)
                    res.append(level)
                    
                    # q.append(current.left)
                    # q.append(current.right)
            # level+=1
        # print(res)
            # print("level",level)
        # print(level)   # res.append(level)
        print(res)
        return 0
        