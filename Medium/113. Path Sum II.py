# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        answer = []
        
        def findSum(node,path):
            if node:
                path.append(node.val)
                if sum(path) == targetSum and node.left == None and node.right == None:
                    answer.append(list(path))
                    return 
                if node.left:
                    findSum(node.left,path)
                    path.pop()
                if node.right:
                    findSum(node.right,path)
                    path.pop()
            else:
                return 0
        # paths = []
        findSum(root,[])
        
        return answer
