import heapq

class Solution:
    def maxTwoEvents(self, events):
        # Sort events by start time
        events.sort()
        
        min_heap = []   # (endTime, value)
        max_val = 0     # max value of non-overlapping event so far
        ans = 0
        
        for start, end, value in events:
            # Remove all events that end before current start
            while min_heap and min_heap[0][0] < start:
                _, v = heapq.heappop(min_heap)
                max_val = max(max_val, v)
            
            # Combine current event with best previous
            ans = max(ans, max_val + value)
            
            # Push current event
            heapq.heappush(min_heap, (end, value))
        
        return ans
