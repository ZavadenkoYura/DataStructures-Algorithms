class CircularQueue(object):
    def __init__(self, n):
        self._capacity = n
        self._data = [0] * self._capacity
        self._head = 0
        self._tail = 0
        self.size = 0


    def __call__(self):
        return self._data

    
    def enqueue(self, element):
        if self.is_full():
            print("ERROR [QUEUE OVERFLOW]")
            return
        self._data[self._tail] = element
        self._tail = (self._tail + 1) % self._capacity
        self.size += 1


    def dequeue(self):
        if self.is_empty():
            print("ERROR [QUEUE UNDERFLOW]")
            return
        value = self._data[self._head]
        self._head = (self._head + 1) % self._capacity
        self.size -= 1
        return value


    def is_empty(self):
        """"
        The check could also be performed as follows:
            self._tail == self._head,
        but for this method to work, one more slot in array should be
        allocated (n + 1) in order to check for a full state properly
        """
        return self.size == 0


    def is_full(self):
        """"
        The check could also be performed as follows:
            (self._tail + 1) % self._capacity == self._head,
        but for this method to work, one more slot in array should be
        allocated (n + 1) in order to check for a full state properly
        """
        return self.size == self._capacity

    def display(self):
        if self.is_empty():
            print("QUEUE EMPTY")
            return

        i = self._head
        while i != self._tail:
            print(self._data[i], end=' ')
            i = (i + 1) % self._capacity


