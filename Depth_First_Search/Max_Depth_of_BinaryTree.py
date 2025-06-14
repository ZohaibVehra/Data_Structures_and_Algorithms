#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

#solution
'''
From the root, our max depth will be the max depth between left and right subtrees + 1.
For any given subtree the max depth similarly is max depth from left/right subtrees + 1.

So we can go recursively down the left and right subtrees, and our return should always
be the depth so far. This means at a node none we return 0, at anything else we return
+1 to the current tracked value
'''

def maxDepth(root) -> int:
    if root == None:
        return 0
    
    Lmax = maxDepth(root.left)
    Rmax = maxDepth(root.right)

    return max(Lmax,Rmax)+1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

print(maxDepth(root))