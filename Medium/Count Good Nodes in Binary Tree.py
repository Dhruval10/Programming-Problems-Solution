# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = []
        
        counter = 0
        
        def dfs(node):
            nonlocal counter
            if node:
                stack.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)                
                if stack and stack[-1] >= max(stack):
                    counter += 1
                stack.pop()
        dfs(root)
        return counter
