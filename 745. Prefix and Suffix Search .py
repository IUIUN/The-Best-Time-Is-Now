//brute force
class WordFilter:

    def __init__(self, words: List[str]):
        self.map = {}
        for idx, word in enumerate(words):
            for x in range(len(word) + 1):
                prefix = word[:x]
                for y in range(len(word) + 1):
                    suffix = word[y:]
                    self.map[prefix + '#' + suffix] = idx

    def f(self, prefix: str, suffix: str) -> int:
        return self.map.get(prefix + '#' + suffix, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

//follow up 我们定义两棵字典树，其中一棵存储正序单词，另一颗存储逆序单词。在构造函数中，我们分别将每个单词的正序和逆序加入到对应的字典树中即可。在f函数中，我们首先找到前缀为prefix的所有单词所对应的索引（其值等同于权重），然后找到后缀为suffix的所有单词所对应的索引。接着的问题就是在这两个索引列表中查找共同最大元素了

class WordFilter:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix: str, suffix: str) -> int:
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)