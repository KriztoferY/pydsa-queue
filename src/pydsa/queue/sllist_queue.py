"""Implementation of the Queue ADT using a singly linked list."""

from typing import Optional, TypeVar, Generic, Generator
from dataclasses import dataclass

from pydsa.queue import IQueue
from pydsa.utils import ElemTypeName


__all__ = (
    'SLListQueue',
)

Elem = TypeVar('Elem')


class SLListQueue(IQueue, Generic[Elem]):
    """
    A generic unbounded queue -- an implementation of the Queue ADT using
    a singly, circularly linked list with a dummy header node.
    """

    @dataclass
    class _Node:
        value: Optional[Elem] = None
        next: Optional["SLListQueue._Node"] = None

    def __init__(self, elem_type: ElemTypeName) -> None:
        """Creates an empty queue.
        """
        # dummy node whose successor is tail node of underlying linked list
        # when queue is not empty, `None` otherwise.
        self._header = SLListQueue._Node()
        self._num_elems = 0
        self._elem_type = elem_type

    def __len__(self) -> int:
        """Returns the number of elements in the queue.

        Returns:
            int: Queue size.
        """
        return self._num_elems

    @property
    def element_type(self) -> ElemTypeName:
        """Name of the type of each element in the queue.
        """
        return self._elem_type

    def _tail(self) -> Optional["_Node"]:
        # Gets the underlying linked list's tail node, which corresponds to
        # the last element at the end of the queue.
        return self._header.next

    def _head(self) -> Optional["_Node"]:
        # Gets the underlying linked list's head node, which corresponds to
        # the first element at the front of the queue.
        tail_node = self._tail()
        return tail_node.next if tail_node else None

    def __iter__(self) -> Generator[Elem, None, None]:
        """Iterates over all elements from the front to the end of the queue.

        Yields:
            The next unprocessed element.
        """
        curr_node = self._head()
        if curr_node is not None:
            for _ in range(len(self)):
                yield curr_node.value
                curr_node = curr_node.next

    def front(self) -> Elem:
        """Gets the element at the front of the queue if it is not empty.

        Returns:
            Elem: The front element.

        Raises:
            RuntimeError: If the queue is empty.
        """
        if self.empty:
            raise RuntimeError('cannot peek front element from empty queue')
        front_node = self._head()
        return front_node.value if front_node else None

    def enqueue(self, elem: Elem) -> None:
        """Inserts an element at the end of the queue.

        Args:
            elem (Elem): The element to insert.
        """
        # create new tail node
        new_node = SLListQueue._Node(elem)
        if not self.empty:
            # link new tail node to head node
            new_node.next = self._head()
            # link old tail node to new tail node
            self._tail().next = new_node
        else:
            # link new tail node to itself as new head node
            new_node.next = new_node
        # link header node to new tail node
        self._header.next = new_node
        # increment counter
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

        # get a handle of old head node and its value
        head_node = self._head()
        value = head_node.value
        # link tail node to successor of old head node
        self._tail().next = head_node.next
        # break old front node's link to new head node
        head_node.next = None
        # decrement counter
        self._num_elems -= 1
        # Help garbage collection
        del head_node

        return value


if __name__ == '__main__':
    from pydsa.queue.queue_demo import run_demo

    q = SLListQueue[int]('int')
    run_demo(q)


""" 
=== OUTPUT ===
element type: 'int'
[3,1,4,1,5]
3 1 4 1 5 
dequeue: front = 3 | size = 5
dequeue: front = 1 | size = 4
dequeue: front = 4 | size = 3
dequeue: front = 1 | size = 2
dequeue: front = 5 | size = 1
[] (queue is empty: True)
"""
