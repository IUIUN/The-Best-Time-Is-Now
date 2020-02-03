gmap = {'Year': 1, 'Month':2, 'Day': 3, 'Hour':4, 'Minute':5, 'Second':6}
class LogSystem:
    def __init__(self):
        self.logs = {}
        

    def put(self, id: int, timestamp: str) -> None:
        ts = tuple(timestamp.split(':'))
        self.logs[ts] = id

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        idx = gmap[gra]
        s = tuple(s.split(':')[:idx])
        e = tuple(e.split(':')[:idx])
        ans = []
        for key in self.logs.keys():
            if s <= key[:idx] <= e:
                ans.append(self.logs[key])
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)