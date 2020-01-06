class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        ret = sorted(d, key=lambda word: (-d[word], word))
        
        return ret[:k]

//better
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        heap = []
        for key, cnt in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, key))
            else:
                if heap[0][0] < cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt, key))
        return [x[1] for x in heap]