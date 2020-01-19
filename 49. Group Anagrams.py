from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for s in strs:
            m[tuple(sorted(s))].append(s)
        return (m.values())