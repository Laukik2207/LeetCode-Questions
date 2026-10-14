# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = ""
        num2 = ""
        temp1 = l1
        temp2 = l2
        while temp1:
            num1+= str(temp1.val)
            temp1 = temp1.next
        while temp2:
            num2 += str(temp2.val)
            temp2 = temp2.next

        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        result = str(num1+num2)[::-1]
        dummy = ListNode(0)
        curr = dummy
        for i in result:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next
         
        