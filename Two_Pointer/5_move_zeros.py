#https://leetcode.com/problems/move-zeroes/

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

#solution
'''
We can have two pointers, one will iterate though the entire list
the other will point to the next position to swap

they both start at 0 and any time we find a non zero i (entire list iterator)
will swap values with the swap pointer and increment it by one

initially this leads to some uneeded swaps, eg if at the first index the value is
5. then as I is non-zero, we will swap them... swapping first index with first index
this does nothing and is wasted, however then we move forward a spot and keep going
eventually this method will ensure all zeros at the end even if it has some redundancy

Note that redundancy does not change the big O runtime thus it isn't worth fixing
'''

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    swap = 0

    for i in range(len(nums)):
        if nums[i] != 0: #swap
            nums[swap], nums[i] = nums[i], nums[swap]
            swap+=1
    
    return


#quick test
nums = [2,0,4,0,9]
moveZeroes(nums)
print(nums)