from collections.abc import Iterable, Iterator
from typing import Any, List


class MyIterator(Iterator):
    def __next__(self):
        ...


class MyList(Iterable):
    def __init__(self):
        self._items: List[Any] = []

    def __iter__(self):
        ...

    def __str__(self):
        return f"{self._items}"


if __name__ == "__main__":
    my_list = MyList()
    print(my_list)
