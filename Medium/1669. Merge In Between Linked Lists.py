# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        partA = list1
        
        for i in range(a-1):
            partA = partA.next
        
        partB = list1
        
        for i in range(b+1):
            partB = partB.next
        
        endList2 = list2
        
        while endList2.next != None:
            endList2 = endList2.next
        
        partA.next = list2
        endList2.next = partB
        
        return list1
