"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict, deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        total_importance = 0
        
        paths = defaultdict(list)
        
        for employee in employees:
            paths[employee.id] = [employee.importance, employee.subordinates]
        
        find_importance = deque()
        find_importance.append(paths[id])
        
        while find_importance:
            importance, subordinates = find_importance.popleft()
            
            total_importance += importance
            
            for subs in subordinates:
                find_importance.append(paths[subs])
                
        return total_importance
