#https://leetcode.com/problems/pacific-atlantic-water-flow/description/
from typing import List

#solution
'''
There are three ways I see to do this
    Either look at every cell and do dfs till we fail or hit ocean(s)
or
    Start from ocean borders and dfs inwards marking each cell 
    repeat from both ends, then any cell with 2 marks is valid
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        validPacific = set()
        validAtlantic = set()
        rows, cols = len(heights), len(heights[0])
        #dfs upwards, aka if water could flow from a point then go to it
        def dfsUpwards(r,c, ocean):
            if (r,c) in ocean: #already checked
                return

            ocean.add((r,c))

            #perform dfs
            if r + 1 < rows and heights[r+1][c] >= heights[r][c]:
                dfsUpwards(r+1,c, ocean)
            if c + 1 < cols and heights[r][c+1] >= heights[r][c]:
                dfsUpwards(r,c+1, ocean)
            if r > 0 and heights[r-1][c] >= heights[r][c]:
                dfsUpwards(r-1,c, ocean)
            if c > 0 and heights[r][c-1] >= heights[r][c]:
                dfsUpwards(r,c-1, ocean)


        for c in range(cols):
            dfsUpwards(0,c, validPacific)
            dfsUpwards(rows-1,c, validAtlantic)
        for r in range(rows):
            dfsUpwards(r,0, validPacific)
            dfsUpwards(r,cols-1, validAtlantic)

        return list(validPacific & validAtlantic)

#test
sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print('input is')
for line in heights:
    print(line)

print(sol.pacificAtlantic(heights))