class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic = dict()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 in dic:
                    dic[sum2].append((i, j))
                else:
                    dic[sum2] = [(i, j)]
        res = set()
        for key in dic:
            value = target - key
            if value in dic:
                list1 = dic[key]
                list2 = dic[value]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if i != k and i != l and j != k and j != l:
                            flist = [nums[i], nums[j], nums[k], nums[l]]
                            flist.sort()
                            res.add(tuple(flist))
        return list(res)