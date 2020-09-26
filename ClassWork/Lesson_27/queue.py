queue = []
queue_start_index = 0

def push(val):
    queue.append(val)

def pop():
    global queue_start_index
    queue_start_index += 1
    return queue[queue_start_index - 1]

def top():
    return queue[queue_start_index]

def size():
    return len(queue) - queue_start_index

def is_empty():
    return len(queue) == 0

def clear():
    queue[:] = []