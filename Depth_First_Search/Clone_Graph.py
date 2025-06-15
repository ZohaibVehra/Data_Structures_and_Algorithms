#https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone_map = {}

        def dfs(curr):
            if curr in clone_map:
                return clone_map[curr]
            
            clone = Node(curr.val)
            clone_map[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)
    
'''struggle to understand return format so no details here'''