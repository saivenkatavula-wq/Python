class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):
        new_node = Node(element)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.head:
            popped_node = self.head
            self.head = self.head.next
            self.size -= 1
            return popped_node.value
        else:
            return "stack is empty"

    def peek(self):
        if self.head:
            return "Stac is empty"
        return self.head.value

    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" --> ")
            currentNode = currentNode.next
        print()


myStack = Stack()
myStack.push('a')
myStack.push('b')
myStack.push('c')

print("linkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("linkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("size", myStack.stackSize())

