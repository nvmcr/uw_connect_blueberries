class RequestQueue:
    def __init__(self) -> None:
        self.queue = []
        pass

    def add(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop()
