class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x:x[0])
        heap = []
        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        return len(heap)
        