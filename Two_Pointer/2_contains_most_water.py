#https://leetcode.com/problems/container-with-most-water/
'''
Given an integer input array heights representing the heights of vertical lines, 
write a function that returns the maximum area of water that can be contained by
two of the lines (and the x-axis). The function should take in an array of 
integers and return an integer.
'''

#Solution
'''
We can start at extreme ends with pointers L and R
every iteration we total the amount of water these two can hold by multiplying the minimum of the two heights with the width 
then we go towards center from whichever side had the smaller height.
Think of it like this, if we had 2 and 5 on the edges, L and R, and at a width of say 10. we can hold a maximum of 2*10 = 20 units of water
No matter how much we move in the right edge, no matter what height we find itll always be less than 20
    Why? 
Because the potential 'container' is limited by the height of the 2, and the width can only get smaller as we go in. 

On the other hand, if we went inwards from the 2 side and hit a 4, now we have min(4,5)*9 = 4*9 = 36!
Therefor the logic is we go inwards from the smaller height every time, if its a tie we can move in both as moving either one results in the limit discussed prior
'''

def most_water(heights):

    #initialize pointers and total variable
    total = 0
    L, R = 0, len(heights)-1

    #loop condition is to never let L and R meet or overlap
    while L<R:
        
        #update total if its greater than before
        total = max(total, (R-L)*min(heights[L],heights[R]))

        #move in on the smaller side
        if heights[L] < heights[R]:
            L+=1
        
        elif heights[L] > heights[R]:
            R-=1
        
        else:
            L+=1
            R-=1
        
    
    return total


#quick test
print(most_water([3,4,1,2,2,4,1,3,2]))