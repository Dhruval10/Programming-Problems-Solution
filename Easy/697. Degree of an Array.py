class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num]=1
            else:
                dict1[num] += 1
        max_key = 0
        max_val = max(list(dict1.values()))
        if max_val == 1:
            return 1
        items = []
        for key,val in dict1.items():
            if val == max_val:
                items.append(key)
        min_dist = math.inf
        for i in range(len(items)):
            left=0
            right=len(nums)-1
            while left <= right:
                if nums[right] != items[i]:
                    right -= 1
                if nums[left] != items[i]:
                    left += 1
                if nums[left] == nums[right] and nums[left]==items[i]:
                    min_dist = min(min_dist, right - left + 1)
                    break
        return min_dist
