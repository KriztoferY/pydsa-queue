# Using a Queue

From the consumers' perspective, the `pydsa-queue` library provides various
ready-to-use queue data structures that can store any kind of Python objects of 
both the primitive and user-defined types. Each queue implementation is a 
subclass of the abstract base class `IQueue`, which defines the common, 
standardized API, except the additional features specific to a particular implementation.

Having chosen an implemented queue type and known the queue element type `T`, 
you instantiate a queue by calling the queue class's constructor with the 
element type described as both generic type hint (the actual type) and a 
constructor argument (one of the string literal defined in 
`pydsa.queue.ElementTypeName`.

```python

from pydsa.queue import CircArrayQueue

q = CircArrayQueue[int](10, 'int')
print(q.elem_type)              # prints int (a string, not type)
```

In this example, the `[int]` part allows runtime type checking to make sure 
all queue elements are `int`s. The second argument `'int'` is one of the 
possible element type category. For the circular array based implementation in
particular, the constructor requires a positive integer as the first argument 
to determine how large a memory chunk should be allocated for the queue storage
to start with.

Now, you've an empty queue `q` awaiting data.

```python
for num in (3, 1, 4, 1):
    q.enqueue(num)

print(len(q))                   # prints 4
```

You may then use the typical idiom to process the elements in the queue in the 
first-in-first-out (FIFO) manner.

```python
while not q.empty():
    print(f'{q.front()} ')
    q.dequeue()
print()                         # prints 3 1 4 1
print(q.empty())                # prints True
```

# Implementing Your Own Queue

By design, all queue types are subclasses of the same abstract class  
`IQueue`, which specifies the interface of a conventional queue
data structure. The class definition of the included implementation 
`pydsa.queue.CircArrayQueue` looks something like this:

```python 
class CircArrayQueue(IQueue, Generic[Elem]):
```

Here, `Elem` specifies the queue element type.

Let's say you're going to define a class `MyQueue` to implement the Queue ADT. 
Here is a blueprint to get you started:

```python

class MyQueue(IQueue, Generic[Elem]):

    def __init__(self, elem_type: ElemTypeName, ...) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Generator[Elem, None, None]:
        pass

    @property
    def element_type(self) -> ElemTypeName:
        pass

    def front(self) -> Elem:
        pass

    def enqueue(self, elem: Elem) -> None:
        pass

    def dequeue(self) -> Elem:
        pass
};
```

To implement the abstract property `elem_type`, you're advised to acquire such
data via the constructor and store it as a private instance field.

This is it!
