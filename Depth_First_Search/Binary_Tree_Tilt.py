#https://leetcode.com/problems/binary-tree-tilt/description/

'''
Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
'''

#solution
'''
For a given node, to calculate its tilt we need to know sum of subtrees
For our final answer we must also add to a total across all nodes
    this can be done with a global variable
For each node, we must calculate tilt, add to global var
    then return sum of all values in that subtree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root) -> int:


        totalTilt = 0
        def helper(node):
            nonlocal totalTilt
            if node == None:
                return 0 #there is no tilt for a non existant node
            
            leftSum = helper(node.left)
            rightSum = helper(node.right)
            totalTilt += abs(rightSum - leftSum)

            return leftSum + rightSum + node.val
        
        helper(root)
        return totalTilt


#test
'''
         21
        /  \
       7    14
      / \   / \
     1   1 2   2
    / \     
   3   3   
'''

root = TreeNode(21)
root.left = TreeNode(7)
root.right = TreeNode(14)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(2)

sol = Solution()
print(sol.findTilt(root))