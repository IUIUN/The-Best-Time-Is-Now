class Solution:
    def frequencySort(self, s: str) -> str:
        st = ''
        c = collections.Counter(s)
        c = sorted(c.items(),key=operator.itemgetter(1),reverse=True)
        print(c)
        for key, value in c:
            st += key * value
        return st

#         s_set = set(s)
#         table = []
#         for val in s_set:
#             table.append((val, s.count(val)))

#         table.sort(key = lambda x: x[1], reverse = True) 

#         return ''.join(map(lambda x: x[0] * x[1], table))