# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        curr3 = None
        head = None
        
        # print(curr1.val)
        # print(curr2.val)
        if curr1 == None and curr2 != None:
            return curr2
        elif curr1 != None and curr2 == None:
            return curr1
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                if head == None:
                    print(curr1.val)
                    head = ListNode(curr1.val)
                    curr3 = head
                    curr1 = curr1.next
                else:
                    print(curr1.val)
                    temp = curr3
                    curr3 = curr1
                    temp.next = curr3
                    curr1 = curr1.next
            elif curr1.val > curr2.val:
                if head == None:
                    print(curr2.val)
                    head = ListNode(curr2.val)
                    curr3 = head
                    curr2 = curr2.next
                else:
                    print(curr2.val)
                    temp = curr3
                    curr3 = curr2
                    temp.next = curr3
                    curr2 = curr2.next
        # Catch cases where one of the linked lists is longer than the other
        while curr1 != None:
            print(curr1.val)
            temp = curr3
            curr3 = curr1
            temp.next = curr3
            curr1 = curr1.next
        while curr2 != None:
            print(curr2.val)
            temp = curr3
            curr3 = curr2
            temp.next = curr3
            curr2 = curr2.next
        
        return head