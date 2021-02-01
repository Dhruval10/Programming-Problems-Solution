# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkSymmetric(root, root)
    
    def checkSymmetric(self, LeftNode, RightNode):
        if LeftNode == None and RightNode == None:
            return True
        if LeftNode == None or RightNode == None:
            return False
        return LeftNode.val == RightNode.val and self.checkSymmetric(LeftNode.left, RightNode.right) and self.checkSymmetric(LeftNode.right, RightNode.left)