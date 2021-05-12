# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        mini = -math.inf
        maxi = math.inf        
        
        def validate(node, mini, maxi):
            if node is None:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            
            return validate(node.left,mini,node.val) and validate(node.right,node.val,maxi)
        
        return validate(root,mini,maxi)
