class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # fast and slow pointers
        slow = head
        fast = head


        # move pointers at respective speeds until they equal other or end of LL
        while fast is not None and fast.next is not None:

            slow, fast = slow.next, fast.next.next

            # cycle exists
            if fast is slow:
                return True

        # No cycle
        return False
