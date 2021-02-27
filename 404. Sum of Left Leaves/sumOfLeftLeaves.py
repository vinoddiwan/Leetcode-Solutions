# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Using BFS (Sai Anish Malla YT)
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        if not root: # Empty Tree
            return result
        
        q = deque([root]) # double deque
        
        while q:
            node = q.popleft()
            
            if node.left:  # left one 
                if not node.left.left and not node.left.right: # left node is leaf
                    result += node.left.val   # add to result
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
        # end
        return result
            
                    
        
