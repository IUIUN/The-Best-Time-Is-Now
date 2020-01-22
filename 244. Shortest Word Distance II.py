class WordDistance:O(mn)

    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1, word2):
        return min([abs(n1 - n2) for n1 in self.d[word1] for n2 in self.d[word2]])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

//O(m+n)
class WordDistance:

    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1, word2):
        l1 = self.d[word1]
        l2 = self.d[word2]
        i, j = 0, 0
        shortest = float('inf')
        while i < len(l1) and j < len(l2):
            shortest = min(shortest, abs(l1[i] - l2[j]))
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return shortest