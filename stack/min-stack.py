class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []    

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if self.minStack[-1] == val:
            self.minStack.pop()
        return val
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# obj = MinStack()
# obj.push(-1)
# x = obj.top()
# y = obj.getMin()
# print(x,y)