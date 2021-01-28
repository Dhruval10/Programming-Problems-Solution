# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def checkTree(node, leftMin, rightMax):
            if node is None:
                return True
            else:
                if node.val <= leftMin or node.val >= rightMax:
                    return False
                else:
                    leftside = checkTree(node.left, leftMin ,node.val)
                    rightside = checkTree(node.right, node.val, rightMax)

                    return leftside and rightside
                
        return checkTree(root, -sys.maxsize, sys.maxsize)