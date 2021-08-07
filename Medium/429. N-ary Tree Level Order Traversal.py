"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        answer = []
        def dfs(node,level):
            if node:
                if len(answer) == level:
                    answer.append([])
                answer[level].append(node.val)
                for child in node.children:
                    dfs(child,level+1)
        dfs(root,0)
        return answer
