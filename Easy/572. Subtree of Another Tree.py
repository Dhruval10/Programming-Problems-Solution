# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def check_similarity(node1,node2):
            if node1 == None or node2 == None:
                return node1 == None and node2 == None
            if node1.val == node2.val:
                return check_similarity(node1.left,node2.left) and check_similarity(node1.right,node2.right)
            elif node1.val != node2.val:
                return False
        if root == None:
            return False
        elif check_similarity(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
