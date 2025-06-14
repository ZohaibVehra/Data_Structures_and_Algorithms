#https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are 
no nodes with a value greater than X. Return the number of good nodes in the binary tree.

Input: 
      3
     / \
    1   4
   /   / \
  3   1   5

Output: 4
Explanation: 
Root Node (3) is always a good node. 4, 3, 5 are also good nodes.

Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''

#solution
'''
At each node, to figure out the amount of good nodes below it we need good nodes
in left and right subtrees of that node. Which means we must return good Left + good Right
    +1 if we are on a good node.

But how to know if we are on a good node? to do so we would need to pass a value downwards.
At each node, to know if its a good node, we need to know the max value on the path to that node.
So we create a helper function that will allow us to pass down a max variable.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_):
            if root == None:
                return 0

            count = 0

            #check if we are at a good node and update max if needed
            if root.val >= max_:
                max_ = root.val
                count+=1
            
            return dfs(root.left, max_) + dfs(root.right, max_) + count

        return dfs(root, root.val)

#test
'''
      3
     / \
    1   4
   /   / \
  3   1   5
'''
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.goodNodes(root))