#https://www.hellointerview.com/learn/code/breadth-first-search/minimum-knight-moves

from collections import deque

'''
We use bfs on all possible knight moves
until we hit target
each level is +1 for moves required
'''

class Solution:
    def minimum_knight_moves(self, x: int, y: int):


        if x==0 and y == 0:
            return 0
        moves = 0        
        directions = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]

        queue = deque([(0,0)])
        visited = set([(0,0)])

        while queue:
            for i in range(len(queue)):
                a, b  = queue.popleft()
                visited.add((a,b))

                if a == x and b == y:
                    return moves

                for dx,dy in directions:
                    if (a+dx,b+dy) not in visited:
                        queue.append((a+dx,b+dy))

            moves+=1
            

        return -1
 
    

#5,2 is 3 moves

sol = Solution()
print(sol.minimum_knight_moves(5,2))