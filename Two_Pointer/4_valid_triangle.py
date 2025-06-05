#https://leetcode.com/problems/valid-triangle-number/description/
'''
Write a function to count the number of triplets in an integer array nums that could
form the sides of a triangle. The triplets do not need to be unique.
'''

#solution
'''
To be a valid triangle we need the two smaller side sums to be less than the 3rd side. 
    so 2 2 4 fails, but 2 2 3 suceeds

example for explanation:  1,2,11,4,9,6,15,18  -> sorted -> 1,2,4,6,9,11,15,18
Start by sorting list

The limiting factor is the size of the largest side so we can start at the largest and work our way down
in other words traverse the list backwards
so for now imagine we do i traversing backwards, therefor the number for i, which ill call I is 18 right now

given a large side, we  can then treat the rest of this like a two sum problem
    if L and R sum be greater than I, then not only is that one valid triangle but so must L = every num between them be!
        in our example L=1 R=15 I=18. that doesnt add up, L+R < 18 so we move L up till we hit L=4 
            now not only is 4 15 18 a triangle, but so is 6 15 18 and 9 15 18 and 11 15 18. so we have r-l added to total
        
        after we get the correct value we just decrement r and repeat

        note that we dont have to start l at 0 again, because if for R=15 L=whatever didnt make it, then as we 
        lower R nothing the left of L would have ever made it again anyway

'''
def triangleNumber(nums):
    nums.sort()
    result = 0
    for i in range(len(nums)-1, 1, -1):
        r = i-1
        l = 0
        
        while l < r:
            if nums[l] + nums[r] > nums[i]: #valid
                result += r-l
                r -=1
            else:
                l+=1
            
    return result


#quick test
nums = [11,4,9,6,15,18]
print(triangleNumber(nums))