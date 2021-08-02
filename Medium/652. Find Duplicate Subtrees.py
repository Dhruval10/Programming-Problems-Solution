# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        paths = []
        mappings = collections.defaultdict(int)
        def dfs(node,path):
            if node:
                path = str(node.val) + "-" + dfs(node.left,path) + '-' + dfs(node.right,path)
                if path in mappings:
                    mappings[path] += 1
                    if mappings[path] == 2:
                        paths.append(node)
                else:
                    mappings[path] = 1
                return path
            else:
                return "#"
        dfs(root,"")
        return paths
