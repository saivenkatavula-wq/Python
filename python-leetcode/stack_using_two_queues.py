import collections
class MyStack(object):

    def __init__(self):
        self.Q1 = collections.deque()
        self.Q2 = collections.deque()
        

    def push(self, x):
        return self.Q1.append(x)
        

    def pop(self):
        if len(self.Q1) == 0:
            return None
        while len(self.Q1) > 1:
            self.Q2.append(self.Q1.popleft())
        top_element = self.Q1.popleft()
        self.Q1 , self.Q2 = self.Q2, self.Q1
        return top_element

        

    def top(self):
        if len(self.Q1) == 0:
            return None
        while len(self.Q1) > 1:
            self.Q2.append(self.Q1.popleft())
        top_element = self.Q1.popleft()
        self.Q2.append(top_element)
        self.Q1 , self.Q2 = self.Q2, self.Q1
        return top_element
        
        

    def empty(self):
        if len(self.Q1) == 0:
            return True
        return False
        
