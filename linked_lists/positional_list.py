class _DoublyLinkedBase:

    class _Node:
        """Only allows 2 properties. Saves memory"""
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, next, prev) -> None:
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0 

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class Empty(Exception):
    """Error attempting to acess an element from an empty container"""
    pass


class PositionalList(_DoublyLinkedBase):

    class Position:
        def __init__(self, container, node) -> None:
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other) -> bool:
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other) -> bool:
            """return True if other does not represent the same location"""
            return not(self == other)

    def _validate(self, p):
        """Return position s node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self. _trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value




        

                
            




