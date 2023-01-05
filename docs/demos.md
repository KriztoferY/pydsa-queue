# Creating & Using Queues

The following demo program shows how to create and perform operations on a
circular array-based queue.

```python title="src/pydsa/queue/circ_array_queue.py"
q = CircArrayQueue[int](4, 'int')

print(f"element type: '{q.element_type}'")

for x in (3, 1, 4, 1, 5):
    q.enqueue(x)

print(q)

for x in q:
    print(f'{x} ', end='')
print()

while not q.empty:
    print(f'dequeue: front = {q.front()} | size = {len(q)}')
    q.dequeue()

print(q, f'(queue is empty: {q.empty})')
```

To run the demo:

```bash
$ python src/pydsa/queue/circ_array_queue.py
```

Output:

```
element type: 'int'
[3,1,4,1,5]
3 1 4 1 5 
dequeue: front = 3 | size = 5
dequeue: front = 1 | size = 4
dequeue: front = 4 | size = 3
dequeue: front = 1 | size = 2
dequeue: front = 5 | size = 1
[] (queue is empty: True)
```
**See Also** : `src/pydsa/queue/linked_list_queue.py` is a similar demo program
using the linked list based implementation instead.

# Merging Two Queues

The following demo program shows how to perform a stable-merge of two (circular
array-based) queues in which the element values imply the priority given when
queues are merged. In the first part, the larger the value, the higher the 
priority (hence the use of `operator.gt` as argument `compare`). In the second 
part, the smaller the value, the higher the priority (hence the use of 
`operator.lt` as argument `compare`).

```python title="src/pydsa/queue/algo/merge.py"
from operator import lt, gt
from pydsa.queue import CircArrayQueue

tests = (
    # larger the value, higher the priority given when merged
    ((4, 7, 2, 10), (3, 6, 8, 9, 5, 1), int, 'int', gt),
    # smaller the value, higher the priority given when merged
    ((4, 7, 2, 10), (3, 6, 8, 9, 5, 1), int, 'int', lt)
)

for nums1, nums2, t, t_name, cmp in tests:
    print(f'compare: {cmp}')
    q1 = CircArrayQueue[t](len(nums1), t_name)
    for num in nums1:
        q1.enqueue(num)
    print(f'q1     : {q1}')

    q2 = CircArrayQueue[t](len(nums2), t_name)
    for num in nums2:
        q2.enqueue(num)
    print(f'q2     : {q2}')

    print('merging q1 and q2...')
    merged = merge(q1, q2, cmp)
    print(f'merged : {merged}')
    print()
```

To run the demo:

```bash
$ python src/pydsa/queue/algo/merge.py
```

Output:

```
compare: <built-in function gt>
q1     : [4,7,2,10]
q2     : [3,6,8,9,5,1]
merging q1 and q2...
merged : [4,7,3,6,8,9,5,2,10,1]

compare: <built-in function lt>
q1     : [4,7,2,10]
q2     : [3,6,8,9,5,1]
merging q1 and q2...
merged : [3,4,6,7,2,8,9,5,1,10]

```
