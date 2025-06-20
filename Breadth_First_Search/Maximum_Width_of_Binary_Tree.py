#https://leetcode.com/problems/maximum-width-of-binary-tree/description/

from collections import deque
from math import inf
from typing import Optional
'''
we must track not only the nodes in a level but their position

root is always 0
then left child must be 0 then 0+1
    so 0, 1
for the next level 0s L child is 0 and R child is 1
    and 1s L  child is 2 and R child is 3. 
pattern is the nodes current position *2 for left child and *2+1 for right

then at the end of each level we compare with some total

note instad of checking currMin every time we could just set it to Q[0]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

    
        if not root: return 0

        Q = deque([(root,0)])
        max_ = 0

        while Q:
            levelSize = len(Q)
            _, currMin = Q[0] 
            for i in range(levelSize):
                node, position = Q.popleft()
                
                #calculate potential max width note its always right most node so w can do this if statement
                if i == levelSize-1:
                    max_ = max(max_, 1+position-currMin)

                if node.left: Q.append((node.left, position*2))
                if node.right: Q.append((node.right, position*2+1))
        
        return max_


#test
'''
         1
       /   \
      3     2
     /       \
    5         9
   /         /
  6         7
'''
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)

root.left.left = TreeNode(5)
root.right.right = TreeNode(9)

root.left.left.left = TreeNode(6)
root.right.right.left = TreeNode(7)
sol = Solution()
print(sol.widthOfBinaryTree(root))

