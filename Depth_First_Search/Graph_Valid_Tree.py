#https://www.lintcode.com/problem/178/

#solution
'''
To see if its a valid tree we must detect for any cycle and also make sure we visited everything
we can keep an array called visited of false to track those, at the end confirming we changed all to true

for the cycle we make a helper function.
for each node, we first add it to visited (make the index true) 
then check if its neighbors have been previously visited, if so instantly returning true
    otherwise we can then run the function on those neighbors.

note we also must pass in the parent (the one from which our current node was called) because as we
loop through neighbors it will be called but this doesnt indicate a cycle.

in other words if 0 connects to 1 2 3 and 1 connects to 0 and 5. theres no cycle but as we go to node 0
its index is set to true in visited, then as we go through its neighbors, hit 1 then go through 
its neighbors, we will again look at 0 and see its been visited. This is expected and okay though

so when we iterate 0's neighbors we pass in the parent as 0 thus when they go through their neighbors
we can say parent != neighbor each time to ignore that case
'''

from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n

        def containsCycle(adj_list, node, visited, parent):
            visited[node] = True

            #for all neighbors of node
            for neighbor in adj_list[node]:
                #cycle detected
                if visited[neighbor] and parent != neighbor:
                    return True
                
                #otherwise check that neighbor too
                elif not visited[neighbor] and containsCycle(adj_list, neighbor, visited, node):
                    return True
                
            return False

        if containsCycle(adj_list, 0, visited, -1):
            return False
        
        return all(visited)
    


#Test
sol = Solution()
print(sol.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))