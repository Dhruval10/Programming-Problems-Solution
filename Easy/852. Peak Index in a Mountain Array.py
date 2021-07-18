class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxi = 0
        for i in range(1,len(arr)):
            if arr[i] >= arr[i-1]:
                maxi = arr[i]
            if arr[i] < arr[i-1]:
                return i-1
