#https://neetcode.io/problems/valid-sudoku?list=neetcode150

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        add to lists of rows cols and sections
        if any have a dupe its failed
        '''
        rowsD = {}
        colsD = {}
        sections = {}

        rows, cols = len(board), len(board[0])

        def segment(x,y):
            if x < 3:
                if y < 3:
                    return 1
                elif y < 6:
                    return 2
                else:
                    return 3
            
            elif x < 6:
                if y < 3:
                    return 4
                elif y < 6:
                    return 5
                else:
                    return 6
            
            else:
                if y < 3:
                    return 7
                elif y < 6:
                    return 8
                else:
                    return 9
            return

        for i in range(rows):
            for j in range(cols):
                valstr = board[i][j]
                if valstr.isnumeric():
                    val = int(valstr)-1
                    if i not in rowsD:
                        rowsD[i] = [0]*9
                    if j not in colsD:
                        colsD [j] = [0]*9
                    
                    seg = segment(i,j)
                    if seg not in sections:
                        sections[seg] = [0]*9
                    
                    rowsD[i][val] += 1
                    if rowsD[i][val] == 2:
                        return False
                    
                    colsD[j][val] += 1
                    if colsD[j][val] == 2:
                        return False

                    sections[seg][val] += 1
                    if sections[seg][val] == 2:
                        return False
            
        return True