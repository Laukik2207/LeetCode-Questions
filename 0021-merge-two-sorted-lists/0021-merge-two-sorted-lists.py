class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        l1 = list1
        l2 = list2

        if l1.val < l2.val:
            dum = l1
            l1 = l1.next
        else:
            dum = l2
            l2 = l2.next

        temp = dum

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1 is not None:
            temp.next = l1
        else:
            temp.next = l2

        return dum