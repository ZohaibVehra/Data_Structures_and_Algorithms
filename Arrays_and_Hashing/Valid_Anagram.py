#https://neetcode.io/problems/is-anagram?list=neetcode150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0]*26
        
        if len(s) != len(t): return False

        for i in range(len(s)):
            chars[ord(s[i].lower())-ord('a')] +=1
            chars[ord(t[i].lower())-ord('a')] -=1

        for val in chars:
            if val !=0: return False
            
        return True