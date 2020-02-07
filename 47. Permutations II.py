def permutations(nums):
    nums.sort()
    res = []
    dfs(nums, [], res)
    return res
def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
if __name__ == "__main__":
    nums = [1,1,2]
    print(permutations(nums))
