#https://www.hellointerview.com/learn/code/two-pointers/3-sum
'''
Given an input integer array nums, write a function to find all unique triplets
[nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, and 
the sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting 
list does not contain any duplicate triplets.
'''

#Solution
'''
We can sort the list which will take Olog(n) time
From there we can go over each number in the list 
and for each number we can look at the nums to the right of them with two pointers 
and sum those to get the target. 
When we find a solution we can add it to a set then move our left and right pointers till they
are on new numbers, since that solution no longer works (duplicate) both must be changed to new numbers
Also at the start of the loop, if our initial number is the same as last iteration we continue to avoid dupes
'''

def threeSum(self, nums):
    nums.sort()
    result = []
    print(nums)
    for i in range(len(nums)-2):  # note its -2 since at the very last 2 we cant have 3 more values

        #ignore duplicate i
        if i>0 and nums[i] == nums[i-1]:
            continue 
        target = -1*nums[i] #L and R must sum to this in order to have them all sum to 0

        L,R = i+1, len(nums)-1

        while L<R:
            Lnum, Rnum = nums[L], nums[R] #for readability

            if Lnum + Rnum > target:
                R-=1

            elif Lnum + Rnum < target:
                L+=1

            else: #solution found
                print(i, L, R)
                print(nums[i], nums[L], nums[R], target)
                result.append([nums[i], nums[L], nums[R]])

                #move L and R and i to new nums
                while L < R and nums[L] == nums[L+1]:
                    L+=1
                while L < R and nums[R] == nums[R-1]:
                    R-=1
                L+=1
                R-=1

    return result
