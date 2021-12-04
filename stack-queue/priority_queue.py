"""Priority queues are often implemented based on heaps but dont nessesarily have to be built on a heap.

A heap is a tree based data structure, where the value of the parent node is greater than or of equal to the children nodes. children nodes can have an equal value. 

Two types of heaps:
min heap - min values are on top
max heap - max values are on top

Priority queues:
binary heap construction - O(n)
polling - O(log(n))


Use hash map to store a positions list of each node value to make removing happen in log(n) time.
Example
{   element value: [positions in the heap],
    2: [0,4,5]}
"""



class PrioriyQueueBase:
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v) -> None:
            self._key = k
            self._value = v

        def __It__(self, other):
            return self._key < other._key

        def is_empty(self):
            return len(self) == 0 
            

