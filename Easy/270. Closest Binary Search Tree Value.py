# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        min_diff = math.inf
        number = math.inf
        
        def traverse(node, min_diff):
            nonlocal number
            if node:
                temp_diff = abs(node.val - target)
                if min_diff > temp_diff:
                    min_diff = temp_diff
                    number = node.val
                traverse(node.left, min_diff)
                traverse(node.right, min_diff)
            else:
                return
        traverse(root, min_diff)
        
        return number
