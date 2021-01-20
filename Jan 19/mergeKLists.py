  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# import queue from PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        all_numbers = []
        head = ListNode(0)
        traversal = head
        
        for i in lists:
            while i:
                all_numbers.append(i.val)
                i = i.next
        
        all_numbers = sorted(all_numbers)                
        
        # print(all_numbers)
        
        i = 0
        while i < len(all_numbers):
            traversal.next = ListNode(all_numbers[i])
            traversal = traversal.next
            i += 1
        
        return head.next
