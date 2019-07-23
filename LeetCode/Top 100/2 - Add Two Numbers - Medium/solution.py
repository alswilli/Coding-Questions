# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def convertToLinkedList(self, totArray):
        head = ListNode(totArray[0])
        curr = prev = head
        
        for val in totArray[1:]:
            curr = ListNode(val)
            prev.next = curr
            prev = curr
            
        return head
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1Array = []
        # l2Array = []
        l1Total = 0
        l2Total = 0
        l1Mult = 1
        l2Mult = 1
        
        while l1 is not None:
            # l1Array.append(l1.val)
            l1Total += l1.val * l1Mult
            l1Mult = l1Mult * 10
            l1 = l1.next
            
        while l2 is not None:
            # l2Array.append(l2.val)
            l2Total += l2.val * l2Mult
            l2Mult = l2Mult * 10
            l2 = l2.next
            
        # print(l1Array)
        # print(l2Array)
        print(l1Total)
        print(l2Total)
        
        total = l1Total + l2Total
        modifier = 10
        totArray = []
        
        print(total)
        
        # if total > 0:
        #     while total > 0:
        #         nodeVal = total % modifier
        #         # modifier = modifier * 10
        #         totArray.append(int(nodeVal))
        #         total = int((total - nodeVal) / 10)
        #         print(total)
        # else:
        #     totArray.append(0)
        
        totalString = str(total)
        i = len(totalString) - 1
        while i >= 0:
            totArray.append(int(totalString[i]))
            i -= 1
            
        print(totArray)  
        
        
        finalList = self.convertToLinkedList(totArray)
        return finalList
                