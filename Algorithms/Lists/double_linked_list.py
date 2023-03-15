class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return f"{type(self).__name__}(data:{self.data}, " \
               f"next_node:{True if self.next_node is not None else False}, " \
               f"prev_node:{True if self.prev_node is not None else False})"


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    @staticmethod
    def insert_after(prev_node: Node, new_data):
        if prev_node is None:
            raise ValueError("prev_node must not be None")
        new_node = Node(new_data)
        new_node.next_node = prev_node.next_node
        new_node.prev_node = prev_node
        prev_node.next_node = new_node

    def append_list(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = new_node
            new_node.prev_node = node

    def print_list(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next_node


if __name__ == '__main__':
    D = DoubleLinkedList()
    D.push(1)
    D.push(2)
    D.push(3)
    D.insert_after(D.head, 2.5)
    D.append_list(5)
    D.append_list(98)
    D.print_list()
