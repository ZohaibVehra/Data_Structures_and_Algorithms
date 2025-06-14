#https://leetcode.com/problems/diameter-of-binary-tree/description/

'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''

#solution
'''
to find the longest path that contains a given node
we would need to know the longest path on the left subtree
and the right, then add those together.
for a tree of 
   1
  2 3
4 5 _ _
from a random node, say 2. we see the max left path is 1 (to 4)
max right is 1 (to 5) therefor the largest possible path is 1+1 = 2

This means from each node, we must return the longest path under it. 
And at each node we must see if the current path is the longest yet.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        longestPath = 0
        
        def helper(node):
            nonlocal longestPath

            if node == None:
                return 0
            
            left = helper(node.left) #returns max path from left
            right = helper(node.right) #returns max path from right

            longestPath = max(longestPath, left+right)

            return max(left, right) + 1
        
        helper(root)
        return longestPath
    

#test
'''
      3
     / \
    1   4
   /   / \
  3   1   5
            \
            100
'''
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(100)

sol = Solution()
print(sol.diameterOfBinaryTree(root))