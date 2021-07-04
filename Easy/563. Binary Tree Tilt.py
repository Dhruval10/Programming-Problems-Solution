# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        totalTilt = 0
        
        def dfs(node):
            nonlocal totalTilt
            
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            tilt = abs(leftSum - rightSum)
            totalTilt += tilt
            
            return leftSum + rightSum + node.val
        
        dfs(root)
        return totalTilt
