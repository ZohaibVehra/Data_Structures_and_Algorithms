#https://neetcode.io/problems/max-area-of-island?list=neetcode150
from typing import List

'''
go through each point waiting to find a 1

if 1 found do dfs
    - add to a 'current tracker'
    - as we go change 1s to 0s to not redo them
    - at the end of the dfs do total = max of current and total
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        total = 0
        current = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            nonlocal current
            if grid[r][c] != 1:
                return
            
            grid[r][c] = 0 #avoid infinite loops
            current +=1

            #dfs
            if r+1 < rows: dfs(r+1,c)
            if c+1 < cols: dfs(r,c+1)
            if r > 0: dfs(r-1,c)
            if c > 0: dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current = 0
                    dfs(i,j)
                    total = max(total, current)
        
        total = max(total,current)
        return total

#test
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
sol = Solution()

print(sol.maxAreaOfIsland(grid))