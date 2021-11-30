class ArrayStack:
    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class Empty(Exception):
    """Error attempting to acess an element from an empty container"""
    pass


def reverseList(l: list=[]):
    stack = ArrayStack()
    for i in l:
        stack.push(i)
    
    reversed_list = []
    while not stack.is_empty():
        val = stack.pop()
        reversed_list.append(val)


    return reversed_list


print(reverseList([1,2,3]))        






