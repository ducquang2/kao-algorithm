# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        ans = temp = ListNode(0)
        while list1 != None and list2 != None: # Check till end
            if  list1.val < list2.val: # Find the smaller val to put in other list
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            # print(temp.val)
        
        temp.next = list1 or list2 # Take any last value from l1 or l2
        
        return ans.next

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
Solution.mergeTwoLists(Solution, l1, l2)
