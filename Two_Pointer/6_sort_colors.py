'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the 
same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''

#Solution
'''
One pointer placeholds red swap and one for white swap. the last one iterates through the list and functions as a blue swap
when our blue swap (B) is a 1 we swap its value with W and then increment both. 
If B is a 0 we swap its value with R, and increment all 3 pointers as increasing the size of the red portion also moves the blue portion
one spot to the right (since red is before blue) but we only increment W if its the same as R, otherwise it may encroach on the B section

Note that there is no posibility that W can be on a 0. This is because any time W is moved right so is B, and if B hit that 0 it wouldve
already swapped with R. 
However, R may be on a 1, as we add 0s we move R to the right, which will encroach on the W section meaning R will be on a 1.
So when we swap next time, we are effectively swapping a 1 into B not a 2, therefor once we swap B and R, we then check if we need to swap
B and W before incrementing any pointers and if so do the swap and increment all pointers

'''

def sortColors(nums) -> None:
        
    r, w = 0,0

    for b in range(len(nums)):   
        if nums[b] == 0: #Red found swap and increment R
            nums[b], nums[r] = nums[r], nums[b]

            if r == w:
                w+=1
            r+=1
            

        if nums[b] == 1: #white found, swap and increment W. note if during red swap we put a 1 on B it is caught now
            nums[b], nums[w] = nums[w], nums[b]
            w+=1


#quick test
nums = [2,1,2,0,0,2,1,0]
sortColors(nums)
print(nums)