# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
       dummy_node = ListNode(1)
       current_node = dummy_node
       
       while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next

        current_node = current_node.next
       if list1 is not None:
        current_node.next = list1
       else:
        current_node.next = list2
            
       return dummy_node.next
