# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        stack, output = [root], []
        
        while stack:
            root = stack.pop()
            if root != None:
                output.append(root.val)   
                if root.right != None:
                    stack.append(root.right)
                if root.left != None:
                    stack.append(root.left)
            
        return output