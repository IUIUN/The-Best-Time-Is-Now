from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0
        

            
//
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def construct_dic(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
        def bfs_words(beginWord, endWord, d):
            queue, visited = deque([(beginWord, 1)]), set()
            while queue:
                word, step = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == endWord:
                        return step
                    for i in range(len(word)):
                        s = word[0:i] + "_" + word[i+1 :]
                        neighbor_word = d.get(s, [])
                        for neighbor in neighbor_word:
                            if neighbor not in visited:
                                queue.append([neighbor, step + 1])
            return 0
        d = construct_dic(wordList)
        return bfs_words(beginWord, endWord, d)