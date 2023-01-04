[![pypi](https://img.shields.io/pypi/v/python-boilerplate.svg)](https://pypi.org/project/python-boilerplate/)
[![python](https://img.shields.io/pypi/pyversions/python-boilerplate.svg)](https://pypi.org/project/python-boilerplate/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/engineer/python-boilerplate/branch/main/graphs/badge.svg)](https://codecov.io/github/engineer/python-boilerplate)

# pydsa-queue

A suite of Python namespaced packages that provides implementations of the Queue ADT and related algorithms.

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
A collection of implementation-agnostic algorithms on the Queue ADT is included in a dedicated module.

```python


```

For more details, visit the [documentation site](https://kriztofery.github.io/pydsa-queue).

Here's what you need to get started.

- [Dependencies](#dependencies)
- [Building \& Testing the Project](#building--testing-the-project)
- [For Developers \& Contributors](#for-developers--contributors)
- [License](#license)
- [Also Want It In Another Language?](#also-want-it-in-another-language)

## Dependencies

Not much. Python 3.7+ is the only dependency.

