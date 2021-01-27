# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        answer = []
        
        def traversal(node, level):
            if not node:
                return
            else:
                if level == len(answer):
                    answer.append([])
                
                answer[level].append(node.val)
                traversal(node.left, level+1)
                traversal(node.right, level+1)
            return answer
                
        return traversal(root, 0)