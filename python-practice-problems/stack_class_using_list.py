class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peak(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# creating a stack:

myStack = Stack()

myStack.push("a")
myStack.push("b")
myStack.push("c")

print("myStack:", myStack.stack)
print("Popped element:", myStack.pop())
print("Stack after pop:", myStack.stack)
print("peek:", myStack.peak())
print("isEmpty", myStack.is_empty())
print("Size of stack:", myStack.size())
