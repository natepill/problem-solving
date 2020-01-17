
"""
    Should refactor solution so that self.min is a Linked List of sorted mins so that if a min
    is deleted from the stack, then we can just adjust self.min accordingly.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None


    def push(self, x: int) -> None:

        if self.min is None:
            self.min = x
            self.data.append(x)

        elif x < self.min:
            self.min = x
            self.data.append(x)
        else:
            self.data.append(x)

    def pop(self) -> None:
        if self.data.pop() is self.min:
            self.min= min(self.data)

    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.min

if __name__ == "__main__":

    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.data)
    print(stack.getMin())
    print(stack.data)
