#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

#solution
'''
we can do this by using bfs, store the current level of nodes in a list 
that appends to a larger return list at the end
simply track when to reverse and when to not with a boolean
'''


from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if not root: return []
        retList = []
        queue = deque([root])
        rev = False

        while queue:
            levelSize = len(queue)
            levelNodes = []

            for i in range(levelSize):
                node = queue.popleft()
                levelNodes.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if rev:
                levelNodes.reverse()
                rev = False
            else:
                rev = True
            
            retList.append(levelNodes)
        
        return retList




#test
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
'''
      3
     / \
    9  20
       / \
      15  7
'''

sol = Solution()
print(sol.zigzagLevelOrder(root))