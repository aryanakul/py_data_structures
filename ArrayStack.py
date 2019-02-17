"""
Python 3 module for implementing a list based LIFO stack.
Stack can grow as long as the python list.
It follows the Adapter Design Pattern.
Based on Data Structures and Algorithms in Python by Goodrich, Tamassia
and Goldwasser.
It requires the custom exception 'Empty' to be imported.
This class provides the following operations on Stack in the following
time complexity:
    S.push(e) -> O(1)*
    S.pop() -> O(1)*
    S.top() -> O(1)
    S.is_empty() -> O(1)
    len(S) -> O(1)
    *amortized
Boilerplate code tests out basic operations provided by the class.
"""
from Empty import Empty


class ArrayStack:
    """ LIFO stack implementation using a python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []     # nonpublic list instance

    def __len__(self):
        """Returns the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)        # new item stored at the end of the list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]       # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()     # remove last item from list

if __name__ == '__main__':
    S = ArrayStack()
    if S.is_empty():
        print("Stack is Empty")
    else:
        print("Stack is not Empty")
    for i in range(10):
        S.push(i)
    print("Length of current stack:", len(S))
    print("Top of current stack:", S.top())
    S.pop()
    print("Length of current stack:", len(S))
    print("Top of current stack:", S.top())
    print("Is the current Stack Empty?", S.is_empty())
    if S.is_empty():
        print("Stack is Empty")
    else:
        print("Stack is not Empty")
