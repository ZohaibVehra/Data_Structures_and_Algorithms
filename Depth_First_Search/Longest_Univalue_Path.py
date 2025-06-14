#https://leetcode.com/problems/longest-univalue-path/description/

'''
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. 
This path may or may not pass through the root.
The length of the path between two nodes is represented by the number of edges between them.

Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
Example 2:
'''

#solution
'''
a global maxPath variable is needed to store current max path

at a given node, for it to be included in the max path 
its left subtree top value must be the same as its own
and the length of the associated path must be given
same with the right

the node must then return 1 if no subtree matches its val
or 1+longest match length if there is a match

but note when we are adding up to see if the current max path is the best, we need to set 
the current val to 0 not 1 like the return variable. The return variable is default 1 as it
counts the connection to the parent node when called, therefor current must = 0 to begin
to not factor in that same connection twice

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root) -> int:
        maxPath = 0
        def helper(node):
            
            nonlocal maxPath

            if node == None:
                return 0

            current = 0
            retMaxPath = 1
           
            leftPath = helper(node.left)
            rightPath = helper(node.right)

            if node.left != None and node.left.val == node.val:
                current += leftPath
                retMaxPath = max(retMaxPath, leftPath+1)

            if node.right != None and node.right.val == node.val:
                current += rightPath
                retMaxPath = max(retMaxPath, rightPath +1)
            
            maxPath = max(maxPath, current)
            return retMaxPath
        
        helper(root)
        return maxPath



#test
'''
        5
       / \
      5   5
     / \    \
    1   1    5
'''
root = TreeNode(5)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)
sol = Solution()
print(sol.longestUnivaluePath(root))
                
            
