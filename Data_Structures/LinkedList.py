class SinglyLinkedListNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self._size = 0
      
    def __len__(self):
        return self._size
        
    def traverse(self):
        head = self.head
        if self.head is None:
            print("The list is empty")
            return
        
        while not(head is None):
            print(head.value, end=" ")
            head = head.next


    def search(self, value):
        head = self.head
        found = None
        while not(head is None):
            if head.value == value:
                found = head
                break
            head = head.next 
        return found        
        
        
    def insert_head(self, value):
        node = SinglyLinkedListNode(value)
        node.next = self.head
        self.head = node
        self._size += 1
        
        
    def insert_tail(self, value):
        node = SinglyLinkedListNode(value)
        if self.head is None:
            self.head = node
        else:
            head = self.head
            while not(head.next is None):
                head = head.next
            head.next = node
            self._size += 1
        
        
    def remove(self, value):
        pass

        
linked_list = SinglyLinkedList()
linked_list.insert_head(1)
linked_list.insert_head(2)
linked_list.insert_head(3)
linked_list.insert_head(4)
linked_list.insert_tail(5)
linked_list.traverse()