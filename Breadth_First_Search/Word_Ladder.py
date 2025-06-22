#complex
#https://neetcode.io/problems/word-ladder?list=neetcode150

from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        bfs from solution outwards returning changes needed as soon as we hit the start word

        take ending word, somehow find all other words in list that is only 1 char off
            +1 moves
        repeat with all those words
            +1 moves
        so on till we hit start word

        perhaps store a giant dictionary, where the key is common words of word length -1 and value is
            can use a number for the rand letter eg 1
            the list of all words that fit, for example a dictionary[ba1] = ["bat", "bag"]

        '''
        if endWord not in wordList or endWord == beginWord:
            return 0

        wordCombinations = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[0:i] + '1' + word[i+1:len(word)]
                if key not in wordCombinations:
                    wordCombinations[key] = []
                wordCombinations[key].append(word)
        #print(wordCombinations, '\n')
        queue = deque([endWord])
        visited = set([endWord])
        moves = 1

        while queue:
            level = len(queue)
            #print(f"queue at level: {level} is {queue}")
            for _ in range(level):
                
                currentWord = queue.popleft()
                #print(f"going into current word: {currentWord}")
                for i in range(len(currentWord)):
                    
                    key = currentWord[0:i] + '1' + currentWord[i+1:len(currentWord)]
                    if currentWord[0:i] + '1' + currentWord[i+1:len(currentWord)] == beginWord[0:i] + '1' + beginWord[i+1:len(beginWord)]: return moves+1
                    #print(key)
                    for word in wordCombinations[key]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)

            moves +=1
            
        return 0

        
        

