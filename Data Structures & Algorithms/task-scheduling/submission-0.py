import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        queue = deque()

        time = 0

        while heap or queue:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq != 0:
                    queue.append((freq, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time
        