class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        l = r = None
        curr = head

        # Identify nodes before `left` and after `right`
        while curr:
            if count == left - 1:
                l = curr
            if count == right + 1:
                r = curr
            curr = curr.next
            count += 1

        # If `left` is the head, adjust `l`
        if not l:
            l = ListNode(0)
            l.next = head
            head = l.next

        x = r
        y = l.next
        temp = y

        # Reverse the sublist
        while temp != r:
            temp = y.next
            y.next = x
            x = y
            y = temp

        l.next = x

        # If `left` was the head, skip the placeholder node
        if l.val == 0:
            return l.next
        return head
