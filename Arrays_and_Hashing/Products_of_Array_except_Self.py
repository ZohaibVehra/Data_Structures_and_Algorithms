#https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        make a new list that replaces elements with the products of all to the right of them
        edit current list to be product of all ements to the left of them
        return a multiplication of both lists
        '''

        rProd = [0]*len(nums)
        

        prodSoFar = 1
        for i in range(len(nums)-1,-1,-1):
            rProd[i] = prodSoFar
            prodSoFar = prodSoFar*nums[i]
        
        prodSoFar = 1
        for i in range(len(nums)):
            val = nums[i]
            nums[i] = prodSoFar*rProd[i]
            prodSoFar = prodSoFar * val



        return nums


        