from queue_.Queue import Queue

queue = Queue()

queue.enqueue(10)
queue.enqueue(4)
queue.enqueue(99)

print(queue)

print('Dequeued: {}'.format(queue.dequeue()))
queue.enqueue(-19)

print(queue)

while not queue.is_empty():
    print('Dequeued: {}'.format(queue.dequeue()))

print(queue)
