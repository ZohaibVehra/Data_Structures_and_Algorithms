#https://leetcode.com/problems/bus-routes/description/

from typing import List
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        '''
        Go from our target, and bfs outwards till we hit our source
        so lets say target = 6

        find every 6, bfs outwards, 1 bus away from 6 means anything in the list with 6.
            if our target is here answer is 1, eg if source =3 and we have  [3 5 6 9] then we just take this one bus from 3 till we hit stop at 6
        
        lets say 3 isnt there, lets say we have these busses [5 6 9] [2 6 7] [3 4 7] [7, 11]

        first step, our source != target so answer isnt 0, need 1 bus at least
        from here, we bfs our initial queue is [0][1] and [1][1] aka every 6 found. 
        
        next we bfs to stuff within the same list so we add the 5,9,2,7 so in this case our qeue becomes for the next level:
            [0][0], [0][2], [1][0], [1][2]  -> note we have seen [0] and [1] entirely, we should not check those again
            if one of these was source, we need to take at least 1 bus. so we must check here too
        
        we then need to expand from there, so that means we must find every 5 9 2 and 7 in other lists 
            we  have a 7 in [2] and [3]. its values are [2][3] and [3][0]
        
        now we must look at the values in that list other than 7, we have 3 4 and 11.
        if these are source we need to take 2 buses
        add to the queue [2][0], [2][1], [3][1]
        we found our answer

        from this pattern we can see that we only need to check for our source when we look at the other lists.


        The pattern seems to be, check all values of a list, if our source is in there return current buses needed to get there
        if not find all other lists associated and check those. we never check a list twice so we need a way to track seen lists

        we need to be able to see a stop and instantly access all associated routes that have it. -> dictionary

        '''
        if source == target:
            return 0

        seenLists = set()
        routeMap = {}

        for route in range(len(routes)):
            for stop in routes[route]:
                if stop in routeMap:
                    routeMap[stop].append(route)
                else:
                    routeMap[stop] = [route]
        
        if target not in routeMap:
            return -1 
            
        queue = deque()
        for route in routeMap[target]:
            queue.append((route, target))
            seenLists.add(route)

        buses = 1
        #bfs
        while queue:
            #print('new Layer', queue)

            level = len(queue)
            for _ in range(level):
                route, parent = queue.popleft()
                #print(f"for route number {route}")
                for stop in routes[route]:
                    #print(f"stop is {stop}")
                    if stop != parent:
                        #check if found
                        if stop == source: return buses

                        #for each route containing that stop add it to queue if we havent seen that route already
                        for routeWithStop in routeMap[stop]:
                            if routeWithStop not in seenLists:
                                seenLists.add(routeWithStop)
                                queue.append((routeWithStop, stop))
            
            #we have finished this layer, so add a required bus
            buses+=1


        return -1



'''
hard problem, not leaving notes and examples for this one, its complex enough that your best bet is going to the link
playing around with it yourself or entering this solution in there and playing around there
'''