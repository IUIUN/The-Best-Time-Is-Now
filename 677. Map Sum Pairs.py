class TrieNode():
    def __init__(self, count = 0):
        self.count = count
        self.children = {}
class MapSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.keys.get(key, 0)
        curr = self.root
        self.keys[key] = val
        for char in key:
            # build the trie tree
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            # Accumulate the value of prefix
            curr.count += delta
        
    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        
        return curr.count
    
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)