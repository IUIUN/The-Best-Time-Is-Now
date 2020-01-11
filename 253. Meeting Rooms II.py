class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[-1] for i in intervals)
        i = cnt = 0
        for s in starts:
            if s < ends[i]: cnt += 1
            else: i += 1
        return cnt
        