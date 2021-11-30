

class ArrayQueue:
    """Creates a circlular queue. This way when removing the first element in the list it doesn't have to move each element behind if forward.
    Might look something like this | None| None| 5| 6| 7| 9| None| None| None| where the front of the queue is 5 and the end is 9."""
    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty:
            raise Empty('Queue is empty')

        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        if 0 < self._size < len(self._data)//4:
            self.resize(len(self._data)//2)
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1


    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front


class Empty(Exception):
    """Error attempting to acess an element from an empty container"""
    pass        



q = ArrayQueue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()



print(q._data)
print(q._front)
print(q._size)