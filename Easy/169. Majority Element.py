class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict1 = {}
        
        max_freq = 1
        max_freq_num = nums[0]
        
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1
                if dict1[nums[i]] > max_freq:
                    max_freq = dict1[nums[i]]
                    max_freq_num = nums[i]
        
        return max_freq_num
