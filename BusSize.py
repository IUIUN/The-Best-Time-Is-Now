
def groupThePeople(input):
    res = []
    def check(size, input):
        if size < max(input):
            return False
        s = 0
        for i in range(len(input)):
            s += input[i]
            if size - s == 0:
                s = 0
        return s == 0
    for size in range(1, sum(input) + 1):
        if sum(input) % size == 0:
            if check(size, input):
                res.append(size)
    
    
    return res if res else []

        

if __name__ == "__main__":
    n = [1,10,11,5,6,4,7]
    print(groupThePeople(n))

              