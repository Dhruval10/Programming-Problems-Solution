# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        array = []
        def dfs(node, array,level):
            if node:
                if len(array) == level:
                    array.append([])
                
                if level % 2 == 0:
                    array[level].append(node.val)
                else:
                    array[level].insert(0,node.val)
                dfs(node.left,array,level+1)
                dfs(node.right,array,level+1)
            
        dfs(root, array,0)
        return array
