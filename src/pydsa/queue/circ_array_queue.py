"""Implementation of Queue ADT using unbounded circular array."""

from typing import Generic, TypeVar, Literal, Generator

from pydsa.queue import IQueue
from pydsa.utils import py_obj_array_type, ElemTypeName

__all__ = (
    'CircArrayQueue',
)

Elem = TypeVar('Elem')


class CircArrayQueue(IQueue, Generic[Elem]):
    """
    A generic unbounded queue -- an implementation of the Queue ADT using
    circular array with a dynamic resizing scheme.
    """

    def __init__(self, init_cap: int, elem_type: ElemTypeName) -> None:
        """Creates an empty queue that can initially store `init_cap` number of
        elements of `elem_type`.

        Args:
            init_cap (int): Initial capacity of the queue.
            elem_type (ElemTypeName): Element type.

        Raises:
            ValueError: If `init_cap` is not a positive integer.
        """
        if init_cap <= 0:
            raise ValueError(
                f'init_cap ({init_cap}) must be a positive integer')

        self._elems = py_obj_array_type(init_cap, elem_type)()
        self._elem_type = elem_type
        self._start_idx = 0
        self._num_elems = 0

    def __len__(self) -> int:
        """Returns the number of elements in the queue.

        Returns:
            int: Queue size.
        """
        return self._num_elems

    def __iter__(self) -> Generator[Elem, None, None]:
        """Iterates over all elements from the front to the end of the queue.

        Yields:
            The next unprocessed element.
        """
        for i in range(len(self)):
            idx = (self._start_idx + i) % self._capacity
            yield self._elems[idx]

    @property
    def _capacity(self) -> int:
        # Returns the maximum number of elements that the queue can store.
        return len(self._elems)

    @property
    def _end_idx(self) -> int:
        # Returns the one-past-the-end position of the queue.
        return (self._start_idx + len(self)) % self._capacity

    def front(self) -> Elem:
        """Gets the element at the front of the queue if it is not empty.

        Returns:
            Elem: The front element.

        Raises:
            RuntimeError: If the queue is empty.
        """
        if self.empty:
            raise RuntimeError('cannot peek front element from empty queue')
        return self._elems[self._start_idx]

    def _resize(self, kind: Literal['grow', 'shrink']) -> None:
        # Realizes the dynamic resizing scheme.
        curr_sz = len(self)
        arr = None
        # Double underlying array if queue is full.
        if kind == 'grow' and curr_sz == self._capacity:
            arr = py_obj_array_type(curr_sz * 2, self._elem_type)()
            for i, elem in enumerate(self):
                arr[i] = elem
        # Shrink underlying array by half if size is no greater than a quarter
        # of the queue's capacity.
        elif (kind == 'shrink'
              and self._capacity >= 2 and curr_sz * 4 < self._capacity):
            arr = py_obj_array_type(self._capacity // 2, self._elem_type)()
            for i, elem in enumerate(self):
                arr[i] = elem

        if arr:
            del self._elems
            self._elems = arr
            self._start_idx = 0

    def enqueue(self, elem: Elem) -> None:
        """Inserts an element at the end of the queue.

        Args:
            elem (Elem): The element to insert.
        """
        self._resize('grow')
        self._elems[self._end_idx] = elem
        self._num_elems += 1

    def dequeue(self) -> Elem:
        """Removes the front element from the queue if it is not empty.

        Returns:
            Elem: The front element removed from the queue.

        Raises:
            RuntimeError: If the queue is empty.
        """
        if self.empty:
            raise RuntimeError('cannot dequeue from an empty queue')

        elem = self._elems[self._start_idx]
        self._num_elems -= 1
        self._start_idx = (self._start_idx + 1) % self._capacity
        self._resize('shrink')
        return elem


if __name__ == '__main__':
    q = CircArrayQueue[int](4, 'int')
    q.enqueue(3)
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(5)
    for x in q:
        print(f'{x} ', end='')
    print()
