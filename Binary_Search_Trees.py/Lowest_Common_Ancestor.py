#https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        if were at a value, 7, and we need 9 or 10 then we know we can go further on the right
            since both are above 7 both must be somewhere on the right 
        if were at value 7 and we need 4 and 6 then we know we can go to the left child since both are below

        if we are on 7 and the values needed are 3 and 10, then we must return 7 since theyre in opposite sides

        in other words as long as we are less than both vals -> right
        greater than both vals -> left
        between vals or on one of them -> ret
        it must exist so we will never hit leaf
        '''
        #print(f"at node {root.val}")
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p,q)
        
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        else: return root

        