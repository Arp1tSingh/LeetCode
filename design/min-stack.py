class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, value: int) -> None:
        if self.stack:

            self.mstack.append(min(value,self.mstack[-1]))
            self.stack.append(value)
        else:
            self.mstack.append(value)
            self.stack.append(value)
        
    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()

    def top(self) -> int:
        
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mstack[-1]
