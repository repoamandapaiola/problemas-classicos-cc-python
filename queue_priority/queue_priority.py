import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)


if __name__ == '__main__':

    q = PriorityQueue()
    q.push('Amanda', 20)
    q.push('Arthur', 10)
    q.push('Mae', 1)
    q.push('Pai', 0)
    q.push('Pai 2', 0)

    print(q.pop())
