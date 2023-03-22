"""
Tree Traversal Iterators
"""


def _is_perfect_length(sequence):
    """
    Get this to work with an empty tree
    """

    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)


def _left_child(index):
    return 2 * index + 1


def _right_child(index):
    return 2 * index + 2


class LevelOrderIterator:
    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                f"a perfect binary tree with length 2^h - 1"
            )
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index += 1
        return result

    def __iter__(self):
        return self


class PreOrderIterator:
    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                f"a perfect binary tree with length 2^h - 1"
            )
        self._sequence = sequence
        self._stack = [0]

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        index = self._stack.pop()
        result = self._sequence[index]

        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = _left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result

    def __iter__(self):
        return self


class InOrderIterator:
    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                f"a perfect binary tree with length 2^h - 1"
            )
        self._sequence = sequence
        self._stack = []
        self._index = 0

    def __next__(self):
        if (len(self._stack) == 0) and (self._index >= len(self._sequence)):
            raise StopIteration

        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)

        index = self._stack.pop()
        result = self._sequence[index]
        self._index = _right_child(index)
        return result


class PostOrderIterator:
    # TODO visit the children first
    pass


missing = object()


class SkipMissingIterator:
    def __init__(self, iterable):
        self._iterable = iter(iterable)

    def __next__(self):
        while True:
            item = next(self._iterable)  # will stop
            if item is not missing:
                return item

    def __iter__(self):
        return self


typesetting_table = {
    "-": "\u2212",
    "*": "\u00D7",
    "/": "\u00F7"
}


class TranslationIterator:
    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iter(iterable)

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)

    def __iter__(self):
        return self


class PerfectBinaryTree:
    def __init__(self, breadth_first_items):
        self._sequence = tuple(breadth_first_items)
        if not _is_perfect_length(self._sequence):
            raise ValueError(
                f"Iterable series of length {len(self._sequence)} does not represent "
                f"a perfect binary tree with length 2^h -1 "
            )

    def __iter__(self):
        return SkipMissingIterator(PreOrderIterator(self._sequence))


if __name__ == '__main__':
    expr_tree = ['*', "+", "-", "a", "b", "c", "d"]
    iterator = LevelOrderIterator(expr_tree)

    for i in iterator:
        print(i)
