# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            newNode = TreeNode(root.val)
            def dfs(node,newNode):
                if node:
                    if node.left:
                        newNode.right = TreeNode(node.left.val)
                        dfs(node.left,newNode.right)
                    if node.right:
                        newNode.left = TreeNode(node.right.val)
                        dfs(node.right,newNode.left)
            dfs(root,newNode)
            return newNode
        else:
            return None
