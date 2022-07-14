# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current = result
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            carry, out =  divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(out)
            current = current.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        # print(result.next)
        return result.next

Solution.addTwoNumbers(Solution, [4,4,3], [6,3,5])