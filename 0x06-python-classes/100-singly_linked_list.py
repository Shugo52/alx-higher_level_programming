#!/usr/bin/python3

"""Creating a Singly linked list in Python"""


class Node:
    """Defines a node of the singly linked list"""

    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self) -> str:
        head = self.__head
        rep = ""

        while head:
            rep += f"{head.data}"
            rep += "\n" if head.next_node else ""
            head = head.next_node

        return rep

    def sorted_insert(self, node):
        """Inserts a new node into a sorted singly linked list."""

        current = self.__head
        prev = None

        # If empty List, node becomes first
        node = Node(node)
        if not current:
            self.__head = node
            return

        # If new node value is greater than list head value
        if current.data > node.data:
            node.next_node = current
            self.__head = node
            return

        # Else increment and check if new node value <= next list node value
        while current.data <= node.data:
            if not current.next_node:
                current.next_node = node
                return

            prev = current
            current = current.next_node
            continue

        # Then new node value is > than current node value
        prev.next_node = node
        node.next_node = current
