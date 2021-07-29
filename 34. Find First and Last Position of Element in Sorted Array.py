class Solution:
    def searchRange(self, array: List[int], target: int) -> List[int]:
        left = 0
        right = len(array)-1
        
        def search(target,left=0):
            right = len(array)-1
            while left <= right:
                mid = (left + right)//2
                if array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        key = search(target,left)
        if key == len(array) or array[key] != target:
            return [-1,-1]
        return [key,search(target+1,key)-1] if target in array[key:key+1] else [-1,-1]
