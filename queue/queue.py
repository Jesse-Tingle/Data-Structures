"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def __str__(self):
        pass

    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value)
            self.head = new_tail
            self.tail = new_tail

        else:
            new_tail = Node(value)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        if not self.head:
            return None

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value

        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value

    def remove_tail(self):
        if not self.tail:
            return None
        current_node = self.head

        if self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value

        else:
            if current_node.next is self.tail:
                current_tail = current_node.next.value
                self.tail = current_node
                current_node.next = None
                return current_tail

    def add_to_head(self, value):
        # If no head / empty list:
        if self.head is None:
            # Create the new node with next = None
            new_node = Node(value, None)
        #  Set self.head = new node
            self.head = new_node
        # Set self.tail = new node
            self.tail = new_node
        # increment self.length
            self.length += 1
        else:
            # If head:
            # Create the new node
            new_node = Node(value, self.head)
        # New_node.next = self.head
        # Set self.head = new_node
            self.head = new_node
        # increment self.length
            self.length += 1

    def remove_at_index(self, index):
        # Remove at index i:
        # 0) Check that length > i. If not, return None
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return target.value
        # Iterate through the loop i-1 times:
        prev_node = self.head
        for i in range(index - 1):
            # This will get us to prev_node points to the node before the target node
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length = self.length - 1
        return target.value


# Array version

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage: List[item] = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # add to tail
#         # append()
#         array = self.storage
#         array.append(value)
#         self.storage = array
#         self.size += 1

#     def dequeue(self):
#         # remove from head
#         # pop()
#         if self.size > 0:
#             array = self.storage
#             removed_value = array.pop(0)
#             self.storage = array
#             self.size -= 1
#             return removed_value

# LinkedList version
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add to tail
        # append()
        current_list = self.storage
        current_list.add_to_tail(value)
        self.storage = current_list
        self.size += 1
        return self.storage

    def dequeue(self):
        # remove from head
        # pop()
        if self.size > 0:
            current_list = self.storage
            removed_value = current_list.remove_head()
            self.storage = current_list
            self.size -= 1
            return removed_value
