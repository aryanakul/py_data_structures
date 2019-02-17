"""
Python 3 module for implementing a list based FIFO queue.
It follows the Adapter Design Pattern.
Based on Data Structures and Algorithms in Python by Goodrich, Tamassia
and Goldwasser.
It requires the custom exception 'Empty' to be imported.
This class provides the following operations on Stack in the following
time complexity:
    Q.enqueue(e) -> O(1)*
    Q.dequeue() -> O(1)*
    Q.first() -> O(1)
    Q.is_empty() -> O(1)
    len(Q) -> O(1)
    *amortized
Boilerplate code tests out basic operations provided by the class.
"""
from Empty import Empty


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    def __init__(self, initial_capacity):
        """Create an empty queue."""
        self._data = [None]*initial_capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is Empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # helps the garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))       # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize the new list of capacity."""
        old = self._data        # keep track of existing list
        self._data = [None]*cap     # allocate list with new capacity
        walk = self._front
        for k in range(self._size):     # only condsidering existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk = (walk + 1) % len(old)    # use old size as modulus
        self._front = 0     # front has been realigned

if __name__ == '__main__':
    Q = ArrayQueue(10)
    if Q.is_empty():
        print("Queue is Empty")
    else:
        print("Queue is not Empty")
    print("Length of underlying array:", len(Q._data))
    for i in range(10):
        Q.enqueue(i)
    print("Length of current queue:", len(Q))
    print("First element of current queue:", Q.first())
    print("Removing element of current queue:", Q.dequeue())
    print("Length of current queue:", len(Q))
    print("First element of current queue:", Q.first())
    for i in range(10, 15):
        Q.enqueue(i)
    print("Is the current Queue Empty?", Q.is_empty())
    print("Length of underlying array:", len(Q._data))
    print("Length of current queue:", len(Q))
    for i in range(12):
        print(Q.dequeue())
    print("Length of underlying array:", len(Q._data))
    print("Length of current queue:", len(Q))
