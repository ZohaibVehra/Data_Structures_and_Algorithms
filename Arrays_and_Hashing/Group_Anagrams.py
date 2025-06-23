#https://neetcode.io/problems/anagram-groups?list=neetcode150

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: return [[""]]

        dic = {}

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c.lower())-ord('a')] +=1
            
            key = tuple(count)
            if key not in dic:
                dic[key] = []

            dic[key].append(s)
           

        ret = []
        for value in dic.values():
            ret.append(value)
        
        return ret
