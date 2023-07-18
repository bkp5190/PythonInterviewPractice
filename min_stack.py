class MinStack:
    def __init__(self):
        self.stack = []  # Initialize the stack

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin() if self.stack else val)))
        # Append a tuple of (value, current_minimum) to the stack

    def pop(self) -> None:
        self.stack.pop()  # Remove the top element from the stack

    def top(self) -> int:
        return self.stack[-1][0]  # Return the value of the top element

    def getMin(self) -> int:
        return self.stack[-1][1]  # Return the current minimum value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
