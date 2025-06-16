#https://leetcode.com/problems/surrounded-regions/description/
from typing import List

#solution
'''
The only way a region is not surrounded by X is if it has Os on the border
so we can look at the border searching for Os then find any region that connects to 
those border Os and mark them as safe in some set.

So we iterate through just the border
    upon finding an O we run our dfs
        if we arent on an X and arent already safe (two Os on border would infinite loop otherwise)
            we will store the position as safe, which means not to be changed to an X
            then dfs through the board for other Os.
    
Finally once we go through all edges, we can iterate through the entire board once
and any position not marked as safe changes to X

'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        safe = set()
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            nonlocal safe

            if board[r][c] == 'X' or (r,c) in safe: 
                return

            safe.add((r,c))

            #if its an O do dfs 
            if r + 1 < rows:
                dfs(r+1,c)
            if c +1 <cols:
                dfs(r,c+1)
            if r > 0:
                dfs(r-1,c)
            if c > 0:
                dfs(r,c-1)
            

        #go over edges
        #row 0 
        for c in range(cols):
            if board[0][c] == "O" and (0,c) not in safe:
                dfs(0,c)
            if board[rows-1][c] == "O" and (rows-1,c) not in safe:
                dfs(rows-1,c)
        
        for r in range(rows):
            if board[r][0] == "O" and (r,0) not in safe:
                dfs(r,0)
            if board[r][cols-1] == "O" and (r,cols-1) not in safe:
                dfs(r,cols-1)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in safe:
                    board[i][j] = "X"
        return
        

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print('starting board')
for line in board:
    print(line)

sol.solve(board)

print('new board')
for line in board:
    print(line)