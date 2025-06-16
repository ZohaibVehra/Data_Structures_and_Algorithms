#https://leetcode.com/problems/flood-fill/description/
from typing import List


#solution
'''
set up directions list to make looking at all directions easier
store the initial value of the first pixel in a global variable for comparison

in the helper, check if we are in bounds and if the value is same as global var
if so, change value, then recall the helper with all directions + current position

note we must check that the original color does not equal the new color, if so just return the image
as is.
we check this because otherwise we get an infinite loop. lets say both are 5
we will check 5 and change it to 5, then go to the left pixel, which if its 5 we also change to 5
but then we go back to the right pixel AGAIN. The idea was we check if right pixel == original color
    and if not that means we changed it already or its not meant to be changed thus we move on
that doesnt work if the original was also 5, because now we see it and think its unchanged, so we get
lost in an inifinite loop
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
      

        directions = (-1,0), (1,0), (0,-1), (0,1)
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        def dfsHelper(pixelR, pixelC):
            nonlocal originalColor
            nonlocal color

            #check within limits
            if pixelR >= 0 and pixelR < len(image) and pixelC >=0 and pixelC < len(image[0]) and image[pixelR][pixelC] == originalColor:
                image[pixelR][pixelC] = color

                #go thru all other directions
                for x,y in directions:
                    dfsHelper(pixelR+x, pixelC+y)
        

        dfsHelper(sr,sc)
        return image

        
#test
sol = Solution()

image = [[1,1,1],[1,1,0],[1,0,1]]

sr = 1
sc = 1
color = 2

print('original')
for line in image:
    print(line)
print('fixed')
image = sol.floodFill(image,sr,sc,color)
for line in image:
    print(line)