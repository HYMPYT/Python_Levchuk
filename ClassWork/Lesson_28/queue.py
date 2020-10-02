Queue = []
QueueStart = 0

def push(val):
    Queue.append(val)

def pop():
    global QueueStart
    if QueueStart > len(Queue) / 2:
        print("**")
        Queue[:QueueStart] = []
        QueueStart = 0

    if QueueStart < len(Queue):
        QueueStart += 1
        return Queue[QueueStart - 1]

def top():
    if QueueStart < len(Queue):
        return Queue[QueueStart]

def size():
    return len(Queue) - QueueStart

def is_empty():
    return len(Queue) - QueueStart == 0

def clear():
    Queue[:] = []


if __name__ == "__main__":
    push(1)
    push(2)
    push(3)
    print(f"Size: {size()}")
    print(pop())
    print(f"Size: {size()}")
    print(pop())
    print(pop())
    print(pop())