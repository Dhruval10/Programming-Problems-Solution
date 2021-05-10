# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        list1 = []
        
        def dfs(node, list1, level):
            if node:
                if len(list1) == level:
                    list1.append([])
                list1[level].append(node.val)
                dfs(node.left,list1,level+1)
                dfs(node.right, list1,level+1)
        dfs(root,list1,0)
        answer = []
        for li in list1:
            answer.append(li[-1])
        return answer
