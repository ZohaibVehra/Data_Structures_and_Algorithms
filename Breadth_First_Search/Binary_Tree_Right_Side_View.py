#https://leetcode.com/problems/binary-tree-right-side-view/description/

from collections import deque
from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
we need to get the right most node for each level.
we can do this by using bfs and for each level we want to store
the last node in that level, assuming we add from left to right
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        if not root:
            return []
        
        queue = deque([root])
        retList = []

        while queue:
            levelSize = len(queue)

            for i in range(levelSize):
                currentNode = queue.popleft()

                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)

                if i == levelSize-1:
                    retList.append(currentNode.val)
        
        return retList
        

#test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

'''
      1
     / \
    2   3
   /
  4
 /
5
'''

sol = Solution()
print(sol.rightSideView(root))
