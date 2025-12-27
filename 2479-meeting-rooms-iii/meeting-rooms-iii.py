import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # available rooms (min-heap)
        available = list(range(n))
        heapq.heapify(available)

        # busy rooms (end_time, room)
        busy = []

        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # free rooms that have finished before current meeting
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + duration, room))

            count[room] += 1

        # room with maximum meetings (smallest index in tie)
        return count.index(max(count))
