def rule(num):
        binary = bin(num).count('1')
        return (binary, num)

if __name__ == "__main__":
        arr = [7,8,6,5]
        print(sorted(arr, key = rule))