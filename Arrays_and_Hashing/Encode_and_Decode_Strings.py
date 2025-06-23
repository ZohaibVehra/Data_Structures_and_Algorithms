#https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        start word with a specific character and length of word followed byt specific char again
        eg for hello ->  #5#  that way we know to copy the next 5 only,
        '''
        s = ''
        for string in strs:
            s+= '#' + str(len(string)) + '#' + string
        
        return s

    def decode(self, s: str) -> List[str]:
        retL = []
        
        i=0
        while i < len(s):
            #print(f"starting while loop i: {i}")
            if s[i] == '#':
                i+=1
                lenS = ''
                while s[i] != '#':
                    lenS += s[i]
                    i+=1
                i+=1 #at the start of the word now
                #print(f"got word length it is {lenS}")
                wordlen = int(lenS)
                word = ''
                while wordlen != 0:
                    #print(f"creating word. so far have {word}")
                    word+=s[i]
                    i+=1
                    wordlen -=1
                #print(f"done making word it is {word} note i is {i}")
                retL.append(word)

        return retL
