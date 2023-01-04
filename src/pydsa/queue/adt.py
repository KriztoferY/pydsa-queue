"""Queue ADT"""

from collections.abc import Sized, Iterable
from typing import TypeVar
from abc import abstractmethod

from pydsa.utils import ElemTypeName

__all__ = (
    'IQueue',
)

Elem = TypeVar('Elem')


class IQueue(Sized, Iterable):
    """
    ``IQueue`` provides an interface for the Queue ADT that supports the
    Pythonic way of iterating over elements and querying collection size.

    Notes:
        Implementations of this ADT must implement the abstract methods 
        ``__len__()``, ``__iter__()``, ``front()``, ``enqueue()``, and 
        ``dequeue()``. In addition, the abstract property ``element_type`` also 
        has to be implemented, and it is suggested to acquire this data via 
        ``__init__()`` with an argument of type ``pydsa.utils.ElemTypeName``.
    """

    @property
    def empty(self) -> bool:
        """Checks if the queue is empty.

        Returns:
            bool: True if the queue contains no elements.
        """
        return len(self) == 0

    def __str__(self) -> str:
        """String representation of the queue, listing elements in queue order
        from left to right.

        Example:
            ``[3,1,4,1,5]``

        Returns:
            str: The string representation.
        """
        s = '['
        if not self.empty:
            itr = iter(self)
            s = f'{s}{next(itr)}'
            for elem in itr:
                s = f'{s},{elem}'
        s = f'{s}]'

        return s

    @property
    @abstractmethod
    def element_type(self) -> ElemTypeName:
        """String representation of the type of each element in the queue.

        Returns:
            Type: The element type string.
        """

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
