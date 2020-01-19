class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1, dic2 = {}, {}
        res_sum = len(list1)+len(list2)
        for i, s in enumerate(list1):
            dic1[s] = i
        for i, s in enumerate(list2):
            if s in dic1:
                tmp_sum = dic1[s] + i
                if tmp_sum < res_sum:
                    res_sum = tmp_sum
                    result = []
                if tmp_sum == res_sum:
                    result.append(s)
                
                # res_sum = min(tmp_sum, res_sum)
                # dic2[tmp_sum] = dic2.get(tmp_sum, []) + [s]
        return result