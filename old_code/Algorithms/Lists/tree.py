class Node:
    def __init__(self, data):
        self.data = data
        self.right_node = None
        self.left_node = None

    def __repr__(self):
        return f"{type(self).__name__} (data:{self.data}, " \
               f"right_node:{self.right_node}, " \
               f"left_node:{self.left_node})"


class BinaryTreeData:
    # left to right
    # less than key

    def __init__(self):
        self.root = None

    def create_tree(self, new_data):
        new_root = Node(new_data)
        self.root: Node = new_root

    def insert_node(self, new_data):
        if self.root is None:
            self.create_tree(new_data)
        else:
            current_node = self.root
            while True:
                parent_node = current_node
                if new_data < parent_node.data:
                    current_node = current_node.left_node
                    if current_node is None:
                        parent_node.left_node = Node(new_data)
                        return
                else:
                    current_node = current_node.right_node
                    if current_node is None:
                        parent_node.right_node = Node(new_data)
                        return

    def search_node(self, find_value):
        current_node = self.root
        while True:
            parent_node = current_node
            if parent_node is None:
                return  # return nothing
            if find_value == parent_node.data:
                return parent_node
            if find_value < parent_node.data:
                current_node = current_node.left_node
            else:
                current_node = current_node.right_node

    def pre_order(self):
        pass

    def in_order(self):
        pass

    def post_order(self):
        pass

    def display(self):
        node = self.root
        while True:
            print(node)
            if node is not None:
                if node.left_node:
                    node = node.left_node
                else:
                    node = node.right_node
            else:
                return


if __name__ == '__main__':
    b = BinaryTreeData()
    b.insert_node(27)
    b.insert_node(14)
    b.insert_node(10)
    b.insert_node(19)
    b.insert_node(35)
    b.insert_node(31)
    b.insert_node(42)
    b.search_node(43)
    # b.display()
