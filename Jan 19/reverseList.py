# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        reversed_list = ListNode(None)
        current = reversed_list
        
        lists = []
        
        while head:
            lists.append(head.val)
            head = head.next
        
        i = 0
        
        # lists = sorted(lists, reverse = True)
        lists = lists[::-1]
        
        while i < len(lists):
            current.next = ListNode(lists[i])
            current = current.next
            i+=1
        
        # current.next = NULL
        return reversed_list.next
