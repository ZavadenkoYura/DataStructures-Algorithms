class Stack(object):    
    def __init__(self, n):
        self._size = n
        self._data = [0] * self._size
        self._top = 0
    
    def __call__(self):
        return self._data[:self._top]
    
    def push(self, element):
        if self._top >= self._size:
            print("ERROR [STACK OVERFLOW]")
            return
        self._data[self._top] = element
        self._top += 1
    
    def pop(self):
        if self.empty():
            print("ERROR [STACK UNDERFLOW]")
            return
        self._top -= 1
        return self._data[self._top]    
    
    def empty(self):
        return self._top <= 0
    
"""
Stack data structure follows the FILO (First In Last Out) policy. Method empty() checks wether the stack
contains no elements. Method pop() removes an element from the top of the stack. If there are no elements
and method pop() is called, stack underflow occurs. If the stack capacity is over predefined size n then 
stack overflow occurs. 
Addition and Deletion of elements are implemented as soft operations by increasing and decreasing variable _top.
All operation on stack are O(1)
"""
