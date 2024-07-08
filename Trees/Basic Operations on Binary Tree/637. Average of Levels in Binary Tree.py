# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res=[]
        q=collections.deque()
        q.append(root)

        if not root:
            return res
        
        while q:
            l=len(q)
            level=[]
            total=0.0
            count=0.0
            for i in range(l):
                # print(i)
                current=q.popleft()
                if current:
                    # print(current.val)
                    # level.append(current.val)
                    total+=current.val
                    count+=1
                    print("total",total,"count",count)
                    q.append(current.left)
                    q.append(current.right)
                    avg=total/count
            if total:
                print("total",total)
                # res.append(level)
                res.append(avg)
            # elif total==0.0:
            #     res.append(0.0)
        # print(res)
        return res