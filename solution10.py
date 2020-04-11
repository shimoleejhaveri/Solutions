"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

Hint 1:
Consider each node in the stack having a minimum value.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.minStack = []

    def push(self, x: int) -> None:
        self.minStack.append(x)

    def pop(self) -> None:
        self.minStack.pop()        

    def top(self) -> int:
        top_val = self.minStack[-1]
        return top_val
        
    def getMin(self) -> int:
        return min(self.minStack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()