# Abstract Data Type & Implementations

The `pydsa.queue` namespace contains:

- Abstract class `IQueue` : Interface for the Queue ADT

- Implementations of the Queue ADT:  

    - Class `CircArrayQueue` : Circular Array Queue
    - Class `LinkedListQueue` : Linked List Queue  

- Utility functions that the above relies upon.

# Algorithms

The `pydsa.queue.algo` namespace contains ADT-implementation-agnostic algorithms on the Queue ADT.

- `merge(queue1, queue2, compare)` : Stable-merges two queues.
