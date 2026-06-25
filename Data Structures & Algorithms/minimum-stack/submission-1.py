class MinStack:

    def __init__(self):
        self.items: list[int] = []
        self.min_items: list[int] = []

    def push(self, val: int) -> None:
        self.items.append(val)
        min_val = min(val, self.min_items[-1] if self.min_items else val)
        self.min_items.append(min_val)

    def pop(self) -> None:
        self.items.pop()
        self.min_items.pop()

    def top(self) -> int:
        return self.items[-1]


    def getMin(self) -> int:
        return self.min_items[-1]
