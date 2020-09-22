class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    s_iter_1 = SimpleIterator(4)
    for i in s_iter_1:
        print(i)