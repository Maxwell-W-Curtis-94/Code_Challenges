class BaseNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"{type(self).__name__} (data:{self.data})"
