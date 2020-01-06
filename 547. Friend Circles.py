class Solution(object):
     def findCircleNum(self, M):
        UF = UnionFind()
        for i in range(len(M)):
            UF.make_set(i)

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    UF.union(i, j)
        return UF.num_sets
    

class Node(object):
    def __init__(self, data, parent = None, rank = 0):
        self.data = data 
        self.parent = parent
        self.rank = rank


class UnionFind(object):
    def __init__(self):
        self.map = {}
        self.num_sets = 0
    
    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.map[data] = node
        self.num_sets += 1

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]
        parent1 = self.find_set_util(node1)
        parent2 = self.find_set_util(node2)
        if parent1.data == parent2.data:
            return
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        self.num_sets -= 1
    
    def find_set_util(self, node):
        parent = node.parent
        if parent == node:
            return node
        node.parent = self.find_set_util(node.parent)
        return node.parent



         


