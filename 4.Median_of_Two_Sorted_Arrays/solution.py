

class Solution:
    def findMedianSortedArrays(
            self, nums1: list[int], nums2: list[int]
    ) -> float:
        arr = sorted(nums1 + nums2)
        length = len(arr)
        if not arr:
            return 0
        if length == 1:
            return arr[0]
        if length % 2 == 1:
            return arr[length // 2]
        else:
            return (arr[length // 2] + arr[length // 2 - 1]) / 2
