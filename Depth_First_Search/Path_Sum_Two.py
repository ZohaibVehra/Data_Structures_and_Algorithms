#https://leetcode.com/problems/path-sum-ii/description/

'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
'''


#solution
'''
by passing down targetSum - nodeVal all the way down a tree, and then checking at
leaf node if it == 0 we can confirm we have a valid path.
In order to add that path to some return list we need to also be passing down a list of node vals
the return list needs to be a global var
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int):
        if root == None:
            return []
            
        retList = []
        def checkPath(node, path, target):
            nonlocal retList

            target = target - node.val #update target
            path = path + [node.val]

            if node.left == None and node.right == None:
                if target == 0: #check for valid path
                    retList.append(path)
                return
            
            if node.left != None:
                checkPath(node.left, path, target)
            
            if node.right != None:
                checkPath(node.right, path, target)
            return
        

        checkPath(root, [], targetSum)
        return retList
    
#test
'''
         5
        / \
       4   8
      /   / \
     11  13  4
    /  \     / \
   7    2   5   1
'''

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

sol = Solution()
print(sol.pathSum(root, 22))