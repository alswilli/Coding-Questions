# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = None
        head2 = None
        
        while head != None:
            if temp == None:
                temp = head
                head2 = temp
                head = head.next
                head2.next = None
                # head2 = temp
            else:
                # temp = head.next
                temp = head
                head = head.next
                temp.next = head2
                head2 = temp
            # head = head.next
        
        return head2
                