class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.curr = self.q1
        self.other = self.q2

    def push(self, x: int) -> None:
        self.curr.append(x)
        

    def pop(self) -> int:
        popped = None
        while self.curr:
            if len(self.curr) > 1:
                self.other.append(self.curr.pop(0))
            else:
                break
        popped = self.curr.pop(0)
        self.curr, self.other = self.other, self.curr
        return popped
        

    def top(self) -> int:
        top = None
        while self.curr:
            popped = self.curr.pop(0)
            self.other.append(popped)
            if len(self.curr) == 0:
                top = popped
                break
        self.curr, self.other = self.other, self.curr
        return top
        

    def empty(self) -> bool:
        return len(self.curr) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()