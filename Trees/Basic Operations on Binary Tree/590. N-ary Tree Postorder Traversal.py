"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]

        def post(root):
            if not root:
                return 
            for i in root.children:
                post(i)
                # res.append(i.val)

            res.append(root.val)
        post(root)
        # print(res)
        return res
        