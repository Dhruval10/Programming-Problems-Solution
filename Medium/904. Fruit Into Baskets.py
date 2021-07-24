class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        bucket = {}
        max_fruits = 0
        left = 0
        right = 0
        while left < len(fruits):
            bucket[fruits[left]] = left
            if len(bucket) >= 3:
                min_value = min(bucket.values())
                del bucket[fruits[min_value]]
                right = min_value + 1
            
            max_fruits = max(max_fruits, left-right+1)
            left += 1
        return max_fruits
