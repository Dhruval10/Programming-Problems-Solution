# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        answer = []
        
        def traversal(node, level):
            if node is None:
                return 
            if level == len(answer):
                answer.append([])
            if level % 2 == 0:
                answer[level].append(node.val)
            if level % 2 != 0:
                answer[level].insert(0,node.val)
            
            traversal(node.left,level+1)
            traversal(node.right, level+1)
            
            return answer
        
        return traversal(root, 0)
