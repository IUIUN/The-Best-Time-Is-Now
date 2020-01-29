class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)
            