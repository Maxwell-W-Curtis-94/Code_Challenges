from collections.abc import Sequence  # get index and count


class SortedFrozenSet(Sequence):
    def __init__(self, items=None):
        self._items = tuple(sorted(
            set(items) if (items is not None)
            else set()
        ))

    def __repr__(self):
        return "{type}({args})".format(
            type=type(self).__name__,
            args=(
                "[{}]".format(
                    ", ".join(
                        map(repr, self._items)
                    )
                )
                if self._items else ""
            )
        )

    def __contains__(self, item):
        return item in self._items

    def __len__(self):  # why not count your self
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items

    def __hash__(self):
        return hash(
            (type(self), self._items)
        )
