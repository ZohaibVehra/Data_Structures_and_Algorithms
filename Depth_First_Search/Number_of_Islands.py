#https://leetcode.com/problems/number-of-islands/description/
from typing import List

#solution
'''
global var to track number of islands found
a visited set to store visited points

we iterate over each value
    in order to not look at same location many times we have two options
        either change the value to 0 as we dfs, or use a visited tracker.
            I'll do option 1 here
    check if its a 1. if so begin dfs
    
in dfs helper func, we continue if within bounds and is 1
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        totalIslands = 0
        rows,cols = len(grid), len(grid[0])

        def dfsHelper(r,c):
            
            #change to 0 to not go over same one again
            grid[r][c] = "0"

            #rerun dfs for every valid position that is a 1
            if r + 1 <rows  and grid[r+1][c] == "1":
                dfsHelper(r+1,c)
            if c + 1 < cols  and grid[r][c+1] == "1":
                dfsHelper(r,c+1)
            if r > 0  and grid[r-1][c] == "1":
                dfsHelper(r-1,c)
            if c > 0  and grid[r][c-1] == "1":
                dfsHelper(r,c-1)
            
            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    totalIslands+=1
                    dfsHelper(i,j)
        
        return totalIslands


sol = Solution()

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print("expecting output = 3    output = ", sol.numIslands(grid))