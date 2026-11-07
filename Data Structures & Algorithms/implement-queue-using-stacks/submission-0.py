class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.curr = self.s1
        self.other = self.s2
        

    def push(self, x: int) -> None:
        self.curr.append(x)
        

    def pop(self) -> int:
        popped = self.curr.pop(0)
        while self.curr:
            self.other.append(self.curr.pop(0))
        self.curr, self.other = self.other, self.curr
        return popped

    def peek(self) -> int:
        popped = self.curr.pop(0)
        self.other.append(popped)
        while self.curr:
            self.other.append(self.curr.pop(0))
        self.curr, self.other = self.other, self.curr
        return popped        

    def empty(self) -> bool:
        return len(self.curr) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()