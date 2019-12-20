class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2)%2 == 1:
            return self.findK(nums1, nums2, (len1 + len2)//2 + 1)
        else:
            return (self.findK(nums1, nums2, (len1 + len2)//2) + self.findK(nums1, nums2, (len1 + len2)//2 + 1))*0.5
    
    def findK(self, nums1, nums2, K):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findK(nums2, nums1, K)
        if len1 == 0:
            return nums2[K-1]
        if K ==1:
            return min(nums1[0], nums2[0])
        pa = min(len1, K//2)
        pb = K - pa
        if nums1[pa -1] <= nums2[pb -1]:
            return self.findK(nums1[pa:], nums2, pb)
        else:
            return self.findK(nums1, nums2[pb:], pa)
        