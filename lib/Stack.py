class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        for item in items:
            if(self.full()):
                return None
            else:
                self.items.append(item)


    
    def isEmpty(self):
        # if (self.items == []):
        #     return True
        # else:
        #     False

        return self.items == []


    def push(self, item):
        if(self.full()):
            return "list is full"
        else:
            self.items.append(item)


    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
    

    def peek(self):
        # return self.items[len(self.items)]

        if self.isEmpty():
            return None
        return self.items[-1]

    
    def size(self):
        return len(self.items)
    

    def full(self):
        if(len(self.items) == self.limit):
            return True
        return False
    

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1
    
    def __repr__(self):
        return f"Stack(items={self.items}, limit={self.limit})"


stk = Stack([1, 2, 3], limit=5)
print(stk.isEmpty())  # Should be False
print(stk.size())     # Should be 3
print(stk.peek())     # Should be 3
print(stk.pop())      # Should be 3
print(stk)
print(stk.size())     # Should be 2
print(stk.search(1))  # Should be 1 (1 is 1 position away from the top)
stk.push(4)
stk.push(5)
print(stk)
print(stk.search(5))  # Should be 0 (5 is at the top)
stk.push(6)
print(stk)
print(stk.push(7))    # Should print "Stack is full" since limit is 5
