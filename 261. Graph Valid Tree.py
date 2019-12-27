import collections

class Solution:
      def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        if n == 0:
            return False
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        queue = [0]
        visited = set()
        while queue:
            curr = queue.pop()
            visited.add(curr)
            queue += [node for node in neighbors[curr] if node not in visited]
        return len(visited) == n
            

            
        