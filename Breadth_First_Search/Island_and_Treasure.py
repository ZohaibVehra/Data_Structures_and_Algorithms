#https://neetcode.io/problems/islands-and-treasure?list=neetcode150

from collections import deque
from typing import List

#due to faster practice no commented solution explanation this time nor test. go to link and test there

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        queue = deque()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
 
        distance = 1
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            level = len(queue)
            for _ in range(level):

                x,y = queue.popleft()

                for dx,dy in directions:
                    nx, ny = x+dx, y+dy

                    if 0 <= nx < rows and 0<= ny < cols:
                        if grid[nx][ny] == inf:
                            grid[nx][ny] = distance
                            queue.append((nx,ny))
            
            distance +=1
        
        return

