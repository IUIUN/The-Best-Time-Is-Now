class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-freq, key) for key, freq in count.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            
        
        
        
