from typing import Callable

from pydsa.queue import IQueue

__all__ = (
    'merge',
)


def merge(queue1: IQueue,
          queue2: IQueue,
          compare: Callable[[IQueue, IQueue], bool]) -> IQueue:
    """Stable-merges two queues.

    Elements are compared using the binary predicate ``compare`` to
    determine the order in which they appear in the merged queue. Relative order
    of elements in the original queues are preserved. A new queue of the same
    type as the two queues to merge is created and returned if both queues to 
    merge are not empty.

    Args:
        queue1 (IQueue): A queue to merge.
        queue2 (IQueue): Another queue to merge.
        compare (Callable[[IQueue, IQueue], bool]): The binary predicate that governs how elements from the original queues are prioritized during merging.

    Returns:
        IQueue: The merged queue.

    Notes:
        The complexity of the merge algorithm is `O(n1 + n2)` in both time and space, where ``n1`` and ``n2`` are the sizes of the two queues to merge.
    """
    n1 = len(queue1)
    n2 = len(queue2)
    if n1 == 0:
        return queue2
    if n2 == 0:
        return queue1

    # Create an empty queue of the same type as input queues
    # to store the merged sequence
    merged = type(queue1)[type(queue1.front())](n1 + n2, queue1.element_type)

    # Compare the elements at the front of two queues
    while not queue1.empty and not queue2.empty:
        queue = queue1 if compare(queue1.front(), queue2.front()) else queue2
        merged.enqueue(queue.front())
        queue.dequeue()

    # Handle unprocessed tail
    queue = queue1 if not queue1.empty else queue2
    while not queue.empty:
        merged.enqueue(queue.front())
        queue.dequeue()

    return merged


if __name__ == '__main__':
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


"""
=== OUTPUT ===
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

"""
