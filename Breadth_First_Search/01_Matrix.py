#https://leetcode.com/problems/01-matrix/description/

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        go from 0s and bfs outwards, only continuing if less than current stored val
        '''

        rows, cols = len(mat), len(mat[0])
        distances = [[-1] * cols for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    queue.append((i,j))
        
        distance = 1

        while queue:
            level = len(queue)
            for _ in range(level):
                x,y = queue.popleft()

                if x>0 and distances[x-1][y] == -1:
                    distances[x-1][y] = distance
                    queue.append((x-1,y))
                if y>0 and distances[x][y-1] == -1:
                    distances[x][y-1] = distance
                    queue.append((x,y-1))
                if x+1 < rows and distances[x+1][y] == -1:
                    distances[x+1][y] = distance
                    queue.append((x+1,y))
                if y+1 < cols and distances[x][y+1] == -1:
                    distances[x][y+1] = distance
                    queue.append((x,y+1))
            
            distance+=1
        
        return distances


mat = [[0,0,0],[0,1,0],[1,1,1]]
sol = Solution()
print(sol.updateMatrix(mat))

