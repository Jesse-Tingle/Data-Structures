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
