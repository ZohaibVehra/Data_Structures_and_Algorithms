#https://neetcode.io/problems/duplicate-integer?list=neetcode150

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = []

        for num in nums:
            if num in dic: return True
            dic.append(num)
        return False