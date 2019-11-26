"""
Author: Kara Meyer
Date: 11-11-2019
Description: Using this program you can create and alter a linked list
"""


class node:
    """Node of a linked list."""

    def __init__(self, data=None):
        """Define how to make a node."""
        self.data = data
        self.next = None


class linked_list:
    """Linked list and methods to alter."""

    def __init__(self, data=None):
        """Initialize the list."""
        first_node = node(data)
        self.head = first_node

    def length(self):
        """Define the length of the list."""
        current_node = self.head
        count = 0
        while current_node.next is not None:
            count += 1
            current_node = current_node.next
        count += 1  # Count the last node
        return count

    def add_tail(self, data):
        """Add a node to the tail of the list."""
        new_node = node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def add_head(self, data):
        """Add a node to the head of the list."""
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def add_index(self, data, index):
        """Add a node at a particular index."""
        if index > self.length():
            print("The index you put in to insert a node is out of range.")
            return
        new_node = node(data)
        current_node = self.head
        for _ in range(index):
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = new_node
        new_node.next = current_node

    def delete_index(self, index):
        """Delete a node at a particular index."""
        if index > self.length():
            print("The index you put in to delete a node is out of range.")
            return
        current_node = self.head
        for _ in range(index):
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = current_node.next
        del current_node

    def value_index(self, index):
        """Get the value at particular index."""
        if index > self.length():
            print("The index you put in is out of range.")
            return
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def print_list(self):
        """Print the list."""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def print_list_and_index(self):
        """Print the list with index."""
        current_node = self.head
        index = 0
        while current_node:
            print(str(index) + ", " + str(current_node.data))
            index += 1
            current_node = current_node.next

    def reverse_list(self):
        """Reverse the list."""
        current_node = self.head.next
        list_length = self.length()
        for _ in range(list_length - 1):
            self.add_head(current_node.data)
            current_node = current_node.next
        for _ in range(list_length - 1):
            self.delete_index(list_length)

    def convert_array(self):
        """Convert a linked list into an array."""
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.data)
            current_node = current_node.next
        return array
