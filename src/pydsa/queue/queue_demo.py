from pydsa.queue import IQueue


def run_demo(queue: IQueue) -> None:
    print(f"element type: '{queue.element_type}'")

    for x in (3, 1, 4, 1, 5):
        queue.enqueue(x)

    print(queue)

    for x in queue:
        print(f'{x} ', end='')
    print()

    while not queue.empty:
        print(f'dequeue: front = {queue.front()} | size = {len(queue)}')
        queue.dequeue()

    print(queue, f'(queue is empty: {queue.empty})')
