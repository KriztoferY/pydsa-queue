from typing import Generic, TypeVar, Literal

from pydsa.queue import IQueue
from pydsa.utils import PyObjArray, ElemTypeName

__all__ = (
    'CircArrayQueue',
)

Elem = TypeVar('Elem')
Q = TypeVar('Q', bound='CircArrayQueue')


class CircArrayQueue(IQueue, Generic[Elem]):

    def __init__(self, init_cap: int, elem_type: ElemTypeName) -> None:
        if init_cap <= 0:
            raise ValueError(
                f'init_cap ({init_cap}) must be positive integer')

        self._elems = PyObjArray(init_cap, elem_type)()
        self._elem_type = elem_type
        self._start_idx = 0
        self._num_elems = 0

    def __len__(self) -> int:
        return self._num_elems

    def __iter__(self):
        for i in range(len(self)):
            idx = (i + len(self)) // self._capacity
            yield self._elems[idx]

    @property
    def _capacity(self) -> int:
        return len(self._elems)

    def _end_idx(self) -> int:
        # Returns the one-past-the-end position of the queue.
        return (self._start_idx + len(self)) // self._capacity

    def front(self) -> Elem:
        if self.empty:
            raise RuntimeError('cannot peek front element from empty queue')
        return self._elems[self._start_idx]

    def _resize(self, kind: Literal['grow', 'shrink']) -> None:
        curr_sz = len(self)
        arr = None
        # Double underlying array if queue is full.
        if kind == 'grow' and curr_sz == self._capacity:
            arr = PyObjArray(curr_sz * 2, self._elem_type)(*self._elems)
        # Shrink underlying array by half if size is no greater than a quarter
        # of the queue's capacity.
        elif kind == 'shrink' and curr_sz * 4 == self._capacity:
            arr = PyObjArray(curr_sz // 2, self._elem_type)(*self._elems)

        if arr:
            del self._elems
            self._elems = arr
            self._start_idx = 0

    def enqueue(self, elem: Elem) -> None:
        self._resize('grow')
        self._elems[self._end_idx] = elem
        self._num_elems += 1

    def dequeue(self) -> Elem:
        if self.empty:
            raise RuntimeError('cannot dequeue from an empty queue')

        elem = self._elems[self._start_idx]
        self._num_elems -= 1
        self._start_idx = (self._start_idx + 1) // self._capacity
        self._resize('shrink')
        return elem


if __name__ == '__main__':
    q = CircArrayQueue[int](-1)
    q.enqueue(12)
    for x in q:
        print(x)
