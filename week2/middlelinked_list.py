def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head
        single = head
        double = head
        while double.next != None:
            single = single.next
            if double.next.next == None:
                return single
            double = double.next.next
        return single
