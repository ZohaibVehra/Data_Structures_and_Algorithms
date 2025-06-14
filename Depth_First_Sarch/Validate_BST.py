# https://leetcode.com/problems/validate-binary-search-tree/
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

#solution
'''
At each node there is a range of values which we must be within
In the tree
 5
/ \
1   10
    / \
    7   17

lets look at the 7. We must be less than 10, but greater than 5.
For the 17 we must be greater than 10, and less than infinity

Each node is given a min max range, first we confirm if we are within it
then for the left child we we update our max to current node value
and for right we update our minimum.
For this we need a helper function to pass down the 2 new varaibles min_ and max_
The info we need to return is simply if our subtree is valid or not in boolean
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        
        def helper(root, min_, max_):
            if root is None:    #base case
                return True
            
            if root.val >= max_ or root.val <= min_:
                return False
            
            #if any false subtree then we continue returning false so
            return helper(root.left, min_, root.val) and helper(root.right, root.val, max_)
        

        return helper(root, float('-inf'), float('inf') )
        

#test
'''
        4
       / \
      2   7
     / \ / \
    1  3 6  9
'''

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
print(sol.isValidBST(root))

#false case
'''
        4
       / \
      2   7
     / \ / \
    1  3 8  9
'''

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(8)
root.right.right = TreeNode(9)

sol = Solution()
print(sol.isValidBST(root))