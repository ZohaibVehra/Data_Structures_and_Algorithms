'''
Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)
Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False
'''

#Solution
'''
Given that the list is sorted, if we take any two spots and add them up we know that by moving to the left the total will decrease, and moving the right will make it increase
With this in mind we can start with two pointers, at both extremes, 0 and length-1. 
From here we can total, if we are too small then the only way to get a larger number is to move the left pointer to the right, and vice versa
By repeating this till we hit the target we can find the solution in one pass of the list

our while loop condition is to keep left below right, as if they meet and come to the solution that is an error since we need a PAIR of numbers to sum up to target
and if they crossover then we are just repeating the totals from before with them swapped
'''

def twoSum(nums, target):
    l, r = 0, len(nums)-1

    while l<r:
        print(l,r)
        if nums[l]+nums[r] > target: #total is too large so we bring r pointer back one spot
            r-=1
        
        elif nums[l]+nums[r] < target: #too small so we move l pointer up one spot
            l+=1
        
        else: #solution
            return [nums[l],nums[r]]
        

    return False



#quick test
print(twoSum([1,3,4,6,9,11],9))