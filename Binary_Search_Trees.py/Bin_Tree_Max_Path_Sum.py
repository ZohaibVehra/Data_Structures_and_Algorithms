#https://neetcode.io/problems/binary-tree-maximum-path-sum?list=neetcode150


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        at a node the max sum is node itself + max sum on left subtree + right if both positive
        note in this -1000 is lowest node val
        '''
        maxPath = -1001

        def dfs(node):
            nonlocal maxPath
            if not node: return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            total = node.val

            if leftMax > 0: total+= leftMax
            if rightMax >0: total+= rightMax
            
            maxPath = max(maxPath, total)

            return max(max(leftMax,rightMax)+node.val, 0)
        
        dfs(root)
        return maxPath