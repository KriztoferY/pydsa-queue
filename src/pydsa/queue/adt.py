"""Queue ADT"""

from collections.abc import Sized, Iterable
from typing import TypeVar
from abc import abstractmethod

__all__ = (
    'IQueue',
)

Elem = TypeVar('Elem')


class IQueue(Sized, Iterable):
    """
    `IQueue` provides an interface for the Queue ADT that supports the
    Pythonic way of iterating over elements and querying collection size.

    Note:
        Implementations of this ADT must implement the abstract methods
        `__len__()`, `__iter__()`, `front()`, `enqueue()`, and `dequeue()`.
    """

    @property
    def empty(self) -> bool:
        """Checks if the queue is empty.

        Returns:
            bool: True if the queue contains no elements.
        """
        return len(self) == 0

    @abstractmethod
    def front(self) -> Elem:
        """Gets the element at the front of the queue if it is not empty.

        Returns:
            Elem: The front element.
        """

    @abstractmethod
    def enqueue(self, elem: Elem) -> None:
        """Inserts an element at the end of the queue.

        Args:
            elem (Elem): The element to insert.
        """

    @abstractmethod
    def dequeue(self) -> Elem:
        """Removes the front element from the queue if it is not empty.

        Returns:
            Elem: _description_
        """
