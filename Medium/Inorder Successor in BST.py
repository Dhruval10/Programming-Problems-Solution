# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        if p.right is not None:
            node = p.right
            successor = node
            while node.left is not None:
                node = node.left
                successor = node
            return successor
        else:
            node = root
            successor = None
            while True:
                if node is None:
                    return None
                if node == p:
                    break
                elif p.val < node.val:
                    successor = node
                    node = node.left
                else:
                    node = node.right

        return successor
