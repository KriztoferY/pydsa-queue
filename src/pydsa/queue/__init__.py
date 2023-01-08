"""Top-level package for Queue and related algorithms."""

from .adt import *  # noqa
from .circ_array_queue import *  # noqa
from .sllist_queue import *  # noqa

__all__ = []
for m in (adt, circ_array_queue, sllist_queue):  # noqa
    __all__.extend(m.__all__)

del adt
del circ_array_queue
del sllist_queue
del m

__all__ = tuple(__all__)
