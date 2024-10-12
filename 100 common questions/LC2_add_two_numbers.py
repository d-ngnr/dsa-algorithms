class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            # Get values
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # New digit
            carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
            
            # Update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

# Example usage
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

print(Solution().addTwoNumbers(l1, l2))