from singly_linked_list import LinkedList


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# Array version

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage: List[item] = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         array = self.storage
#         array.insert(0, value)
#         self.storage = array
#         self.size += 1

#     def pop(self):
#         if self.size > 0:
#             array = self.storage
#             removed_value = array.pop(0)
#             self.storage = array
#             self.size -= 1
#             return removed_value


# LinkedList version

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        current_list = self.storage
        current_list.add_to_head(value)
        self.storage = current_list
        self.size += 1
        return self.storage

    def pop(self):
        if self.size > 0:
            current_list = self.storage
            removed_value = current_list.remove_head()
            self.storage = current_list
            self.size -= 1
            return removed_value
