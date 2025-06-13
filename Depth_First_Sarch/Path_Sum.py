#https://leetcode.com/problems/path-sum/description/
'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
such that adding up all the values along the path equals targetSum. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is 2-11-4-5.
'''

#solution
'''
Lets assume we are going down the right path.
If so, adding up values from root to leaf we should get targetSum

in other words, if at the start we do targetSum -= node.val when we hit the leaf
we need to be at 0 for that to be a valid path.

So we can do this process down the node, and if were at a leaf we can return 
true or false depending on our result. Now each leaf spits our true or false

then in a non leaf scenario, we spit out true if we got any true in the left or right
since either way means we have one valid path
'''

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
            if root == None:    #in a scenario with one side having child it is not a leaf
                return False

            targetSum -= root.val #subtract this nodes value

            if root.left == None and root.right == None: #leaf spotted
                return targetSum == 0
            
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    


#quick test
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# build test tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

sol = Solution()
print(sol.hasPathSum(root, 22))