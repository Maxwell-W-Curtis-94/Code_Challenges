from Algorithm.LinkedLists.base_node import BaseNode


class LinkedList:
    """
    TODO
    implement collection protocol
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"{type(self).__name__} (head->{self.head})"

    def push(self, data):
        new_node = BaseNode(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_after(self, data, prev_node):
        if prev_node is None:
            raise ValueError()
        new_node = BaseNode(data)
        new_node.next_node = prev_node.next_node
        prev_node.next_node = new_node

    def append_list(self, data):
        new_node = BaseNode(data)
        if self.head is None:
            self.head = new_node
        else:
            hold_node = self.head
            while hold_node.next_node:
                hold_node = hold_node.next_node
            hold_node.next_node = new_node

    def print_list(self):
        node = self.head
        while True:
            if node is None:
                break
            print(node)
            node = node.next_node
