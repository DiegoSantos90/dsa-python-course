''''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Time Complexity: O(1) for all operations
Space Complexity: O(n) for storing elements in the stack
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.min_stack[-1], val) if self.min_stack else val
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    min_stack = MinStack()
    print(min_stack.push(-2))
    print(min_stack.push(0))
    print(min_stack.push(1))
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin())
