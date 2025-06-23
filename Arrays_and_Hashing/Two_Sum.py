#https://neetcode.io/problems/two-integer-sum?list=neetcode150

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for index, val in enumerate(nums):
            dic[val] = index

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in dic and dic[needed] != i:
                return [i,dic[needed]]