
def groupThePeople(groupSizes):
    res = []
    for size in range(1, max(groupSizes) + 1 ):
        temp = []
        for i in range(len(groupSizes)):
            if groupSizes[i] == size and len(temp) < size:
                temp += [i]
            elif groupSizes[i] == size and len(temp)==size:
                res += [temp]
                temp = [i]
        if temp != []:
            res += [temp]
    return res

if __name__ == "__main__":
    n = [3,3,3,3,3,1,3]
    print(groupThePeople(n))

                              
  //
  class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]               