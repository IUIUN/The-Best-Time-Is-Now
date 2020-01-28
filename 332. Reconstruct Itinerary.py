class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for key, value in tickets:
            graph[key].append(value)
        for frm, tos in graph.items():
            tos.sort(reverse = True)
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]
    def dfs(self, graph, start, res):
        while graph[start]:
            v = graph[start].pop()
            self.dfs(graph, v, res)
        res.append(start)

