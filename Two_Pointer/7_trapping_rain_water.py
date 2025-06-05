#https://leetcode.com/problems/trapping-rain-water/description/
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

#solution
'''
To get the amount of water trapped in a given column, we do the following equation
    trapped water = min(max height on left, max height on right) - height of current column
    in other words if we have 4 2 1 3  and went water in the one column. we find the min height 
    of the highest columns on left and right of 1, in this case the highest on left is 4, and right is 3
    the minimum of those is 3. so we have 3 units height that may contain water, we subtract the 1 from that
    as whatever space the column takes cannot be water, so we get 3 - 1 = 2.
    water = min(maxL, maxR) - current

This method means we need to know the max on the left and right at all times, one way to do this is to start there
we have pointers L and R on the extremes. Any time they move they update maxL and maxR respectively. 
if our extremes are 5 and 3 lets think what may happen. of course on the extremes we have no water
    because at edges maxL = maxR = 0
but if we move L in one what may it be? well theres 2 options. if somewhere in there we have a value above 5
    then it will be 5 - column. It cannot exceed 5 as it is limited by the maxL which at that point will be 5
    but it may also be 3 or 4. 3 if we have no values above 3 as then its limited by maxR = 3, 4 if we have a 4 in there

On the other hand if we look at moving the 3 in, it can ONLY be 3. if there is a 2 on the left, maxL will still be 5, and 
if its maxL is 5 we still get 3 since maxR is 3. We cant go lower. We also cant go higher since were limited by the 3.

In other words, whichever is lower of maxL and maxR can be moved in and at that point we can calculate water.
    if equal we can move either in, lets just say L

We can do a loop of this while making sure L and R dont meet
    '''

def trap(height) -> int:

    L, R = 0, len(height)
    total = 0
    maxL, maxR = height[0], height[-1]
    while R-L > 1: #if R is 3 and L is 2, we dont want to move in or theyll overlap
        if maxL <= maxR: #move L in
            L+=1
            #calculate added water
            total += max(0, maxL - height[L])
            #set new max if we have one
            maxL = max(maxL, height[L])
        
        else: 
            R-=1
            #calculate added water
            total += max(0, maxR - height[R])
            #set new max if we have one
            maxR = max(maxR, height[R])
    
    return total


#quick test
print(trap([3, 4, 1, 2, 2, 5, 1, 0, 2]))