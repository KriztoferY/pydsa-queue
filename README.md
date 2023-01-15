[![pypi](https://img.shields.io/pypi/v/pydsa-queue.svg)](https://pypi.org/project/pydsa-queue/)
[![python](https://img.shields.io/pypi/pyversions/pydsa-queue.svg)](https://pypi.org/project/pydsa-queue/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/engineer/pydsa-queue/branch/main/graphs/badge.svg)](https://codecov.io/github/engineer/pydsa-queue)

# pydsa-queue <!-- omit in toc -->

<!--intro-start-->

## Introducing PyDSA - Queue <!-- omit in toc -->

**PyDSA - Queue** (`pydsa-queue`) is a suite of Python namespaced packages that provides implementations of the Queue ADT and related algorithms.

Two implementations of the Queue ADT are included in the project off the shelf:

* `CircArrayQueue` : Circular array based implementation

* `SLListQueue` : Singly linked list based implementation

Different implementations of the Queue ADT are defined in separate modules.

```python
from pydsa.queue import CircArrayQueue

q = CircArrayQueue[int](4, 'int')

print(f"element type: '{q.element_type}'") # ~> "element type: 'int'"

for x in (3, 1, 4, 1, 5):
    q.enqueue(x)

print(q)                                   # ~> "[3,1,4,1,5]"

for x in q:
    print(f'{x} ', end='')
print()                                    # ~> "3 1 4 1 5"

while not q.empty:
    print(f'dequeue: front = {q.front()} | size = {len(q)}')
    q.dequeue()

print(q, f'(queue is empty: {q.empty})')   # ~> "[] (queue is empty: True)"

```
A collection of ADT-implementation-agnostic algorithms on the Queue ADT is 
included in a dedicated module.

```python
from operator import gt

from pydsa.queue import CircArrayQueue
from pydsa.queue.algo import merge

nums1 = (4, 7, 2, 10)
q1 = CircArrayQueue[int](len(nums1), 'int')
for num in nums1:
    q1.enqueue(num)

nums2 = (3, 6, 8, 9, 5, 1)
q2 = CircArrayQueue[int](len(nums2), 'int')
for num in nums2:
    q2.enqueue(num)

merged = merge(q1, q2, gt)
print(f'merged : {merged}')     # ~> "merged : [4,7,3,6,8,9,5,2,10,1]"
```
<!--intro-end-->

For more details, visit the <a href="https://KriztoferY.github.io/pydsa-queue" target="_blank">documentation site</a>.

<!--intro-start-->

## Getting Started <!-- omit in toc -->

Here's what you need to get started.

- [Dependencies](#dependencies)
- [Installation](#installation)
- [License](#license)

### Dependencies

Not much. Python 3.7+ is the only dependency.

### Installation

Just use `pip`.

```python
pip install -U pydsa-queue
```

### License

`pydsa-queue` is licensed under the <a href="https://github.com/KriztoferY/pydsa-queue/blob/main/LICENSE" target="_blank">BSD 3-Clause License</a>.

## Also Want It In Another Language? <!-- omit in toc -->

- C : <a href="https://github.com/KriztoferY/cdsa-queue" target="_blank">Repository</a> | <a href="https://KriztoferY.github.io/cdsa-queue" target="_blank">Documentation</a>
- C++ : <a href="https://github.com/KriztoferY/cppdsa-queue" target="_blank">Repository</a> | <a href="https://KriztoferY.github.io/cppdsa-queue" target="_blank">Documentation</a>
- Go : <a href="https://github.com/KriztoferY/godsa-queue" target="_blank">Repository</a> | <a href="https://KriztoferY.github.io/godsa-queue" target="_blank">Documentation</a> [coming soon]
- TypeScript : <a href="https://github.com/KriztoferY/tsdsa-queue" target="_blank">Repository</a> | <a href="https://KriztoferY.github.io/tsdsa-queue" target="_blank">Documentation</a>

<!--intro-end-->