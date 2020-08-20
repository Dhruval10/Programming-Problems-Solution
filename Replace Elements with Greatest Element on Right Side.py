# Solution exectes in 24 ms and 132 ms for very large 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,0,-1):
            if arr[i] > arr[i-1]:
                arr[i-1] = arr[i]
        del arr[0]
        arr += [-1]
        return arr
