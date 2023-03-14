class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"{type(self).__name__} (data:{self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"{type(self).__name__} (head->{self.head})"

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    @staticmethod
    def insert_after(prev_node: Node, new_data):
        if prev_node is None:
            raise ValueError("prev_node must not be None")
        new_node = Node(new_data)
        new_node.next_node = prev_node.next_node
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

    def print_list(self):
        node = self.head
        while True:
            if node is None:
                break
            print(node)
            node = node.next_node


if __name__ == '__main__':
    l = LinkedList()
    l.push(1)
    l.push(2)
    l.push(3)
    l.insert_after(l.head, 2.5)
    l.append_list(0)
    l.print_list()
