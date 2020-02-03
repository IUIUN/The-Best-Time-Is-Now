import collections
def smallestRange(nums):
        v = list()
        k = len(nums)
        for i in range(len(nums)):
            for num in nums[i]:
                v.append((num, i))
        v.sort()
        l, r, n = 0, 0, len(v)
        cnt = 0
        min_len = float('inf')
        res = [0, 0]
        d = collections.defaultdict(int)
        while r < n:
            if d[v[r][1]] == 0:
                cnt += 1
            d[v[r][1]] += 1
            while l <= r and cnt == k:
                if v[r][0] - v[l][0] < min_len:
                    min_len = v[r][0] - v[l][0]
                    res = [v[l][0], v[r][0]]
                d[v[l][1]] -= 1
                if d[v[l][1]] == 0:
                    del d[v[l][1]]
                    cnt -= 1
                l += 1
            r += 1
        return res
if __name__ == "__main__":
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    print(smallestRange(nums))