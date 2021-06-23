# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        array = []
        
        def traverse(node):
            if node:
                if len(array) < k:
                    heapq.heappush(array,[-abs(target-node.val),node.val])
                else:
                    heapq.heappushpop(array,[-abs(target-node.val),node.val])
                traverse(node.left)
                traverse(node.right)
            else:
                return
        traverse(root)
        
        answer = [i[1] for i in array]
        
        return answer
