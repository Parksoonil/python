from calendar import c


class MyCirCularQuene:
    def __init__(self, i: int):
        self.q = [None] * i
        self.maxlen = i
        self.p1 = 0
        self.p2 = 0
    def enQuene(self, val: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = val
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
    def deQuene(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

circularQuene = MyCirCularQuene(5)
print(circularQuene.enQuene(10))
print(circularQuene.enQuene(20))
print(circularQuene.enQuene(30))
print(circularQuene.enQuene(40))
print(circularQuene.Rear())
print(circularQuene.isFull())
print(circularQuene.deQuene())
print(circularQuene.deQuene())
print(circularQuene.enQuene(50))
print(circularQuene.enQuene(60))
print(circularQuene.Rear())
print(circularQuene.Front())

