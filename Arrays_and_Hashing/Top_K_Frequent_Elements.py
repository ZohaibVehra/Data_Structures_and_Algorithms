#https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 0
            
            dic[num]+=1

        
        freq = [[] for i in range(len(nums)+1)]

        for value, count in dic.items():
            freq[count].append(value)
        
        retL = []

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                retL.append(num)
                if len(retL) == k:
                    return retL
        
        return retL