# I didn’t just brute-force it… I obliterated it with the most brutal brute force imaginable 😂
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        newL1 = []
        newL2 = []
        currentNode1 = l1
        currentNode2 = l2
        while currentNode1:
            newL1.append(currentNode1.val)
            currentNode1 = currentNode1.next
        while currentNode2:
            newL2.append(currentNode2.val)
            currentNode2 = currentNode2.next
        reverse_L1 = newL1[::-1]
        final_L1 = int("".join(str(num) for num in reverse_L1))
        reverse_L2 = newL2[::-1]
        final_L2 = int("".join(str(num) for num in reverse_L2))
        pre_final_list = str(final_L1 + final_L2)
        final_list = pre_final_list[::-1]
        
        dummy_node = ListNode(-1)
        current_node = dummy_node
        
        for val in final_list:
            current_node.next = ListNode(int(val))
            current_node = current_node.next
        return dummy_node.next
