def addBinary(a, b):
        i, j = len(a)-1, len(b)-1
        s = 0
        res = ''
        while i >= 0 or j >= 0 or s != 0:
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            res += str(s % 2)
            s //= 2
        return "".join(res[::-1])
if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(addBinary(a, b))