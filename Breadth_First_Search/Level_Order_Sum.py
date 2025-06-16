#https://www.hellointerview.com/learn/code/breadth-first-search/level-order-sum
from collections import deque



class Solution:
    def level_order_sum(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            sum = 0

            for i in range(level_size):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(sum)
        return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Simple so i wont bother with test, this is just to learn basics of dfs in binary trees

general gist is, use a deque to store nodes to pop in dfs order by using popleft
to keep track of the level we're one, we see the length of the queue at the start
and loop that many times only (that covers the level). of course in the loop we add the next level to the queue
but after the for loop we make note of the current level being finished before the next part starts and we
get the len of queue again to do the next level
'''
