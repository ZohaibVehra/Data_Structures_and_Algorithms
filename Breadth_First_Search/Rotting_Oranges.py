from collections import deque
from typing import List

#https://leetcode.com/problems/rotting-oranges/description/

#solution
'''
BFS
go through grid and locate all rotting oranges, put them in queue
store all non rotting oranges in a set

start bfs from queue, and take note of level, every level finish add a minute
in the bfs, we only go values in the non rotting oranges set. (O(1) look up)

when bfs ends check length of non rotting set, if 0 return minutes, else return -1
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        queue = deque() #for bfs
        healthy = set() #healthy oranges
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1: healthy.add((i,j))
                elif grid[i][j] == 2: queue.append((i,j))
        
        minutes = -1
        if len(healthy) == 0:
            return 0

        while queue:
            level = len(queue)          

            for _ in range(level):
                x,y = queue.popleft()

                if x>0 and (x-1,y) in healthy:
                    healthy.remove((x-1,y))
                    queue.append((x-1,y))
                if y>0 and (x,y-1) in healthy:
                    healthy.remove((x,y-1))
                    queue.append((x,y-1))
                if x+1 < len(grid) and (x+1,y) in healthy:
                    healthy.remove((x+1,y))
                    queue.append((x+1,y))
                if y+1 < len(grid[0]) and (x,y+1) in healthy:
                    healthy.remove((x,y+1))
                    queue.append((x,y+1))
                
            minutes +=1
        
        if len(healthy) == 0:
            return minutes
        return -1
                
sol = Solution()
grid = grid = [[2,1,1],[1,1,0],[0,1,1]]
for line in grid:
    print(line)

print()
print(sol.orangesRotting(grid))

