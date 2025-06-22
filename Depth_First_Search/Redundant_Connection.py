#complex
#https://neetcode.io/problems/redundant-connection?list=neetcode150

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        dfs to find a cycle,
        return all edges part of a cycle somehow
        then return the last one in edges 

        how to know which edge is part of a cycle though?
        track the parents in a list, in ex 2, from 1 we go to 2, and pass in [1] as parent
            it ends there since 2 has no other connection
        then we go to 3 and pass [1] as parent. then we go to 4 and pass [1,3] 
        then we go to 1 and it is in visited already. so we have current = 4, parents = [1,3] going to [1]
            from here we can get a list of all edges in that path, 1,3  3,4  4,1 
            we can break any of those so check our edges for which comes last
        '''
        if len(edges) == 0: return []

        adj_list = {}
        for u,v in edges:
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            adj_list[u].append(v)
            adj_list[v].append(u)

        removable = []
        visited = set()

        def findCycleEdges(node, parents, visited, removable, adj_list):
            visited.add(node)
            parents.append(node)
            #print(f"starting for node {node} with parents {parents}")

            for child in adj_list[node]:
                #print(f"for child: {child}, node rn is {node}")

                if child != parents[-2] and child in visited: #cycle found
                    #print(f"child in visited, cycle found, child: {child}, parents is {parents} from node {node}")
                    start = False
                    for i in range(1,len(parents)-1):
                        if parents[i] == child: start = True

                        if start:
                            removable.append([parents[i],parents[i+1]])
                            removable.append([parents[i+1],parents[i]])
                    removable.append([node,child])
                    removable.append([child,node])

                if child != parents[-2] and child not in visited:
                    #print(f"child not in visited : {child}")
                    findCycleEdges(child, parents.copy(), visited, removable, adj_list)
                
        

        findCycleEdges(1,[-1],visited, removable, adj_list)
        
        last_index = 0
        for i in range(len(edges)):
            if edges[i] in removable:
                #print(f'found at edge {edges[i]}')
                last_index = i
        return edges[last_index]

