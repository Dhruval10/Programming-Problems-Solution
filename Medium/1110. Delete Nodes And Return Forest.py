# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        answer = []
        toDelete = set(to_delete)
        def dfs(node):
            if not node:
                return None
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)
            if node.val in toDelete:
                if node.left:
                    answer.append(node.left)
                if node.right:
                    answer.append(node.right)
                return None
            return node
        dfs(root)
        if root.val not in toDelete:
            answer.append(root)
        return answer
