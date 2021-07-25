class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        left_ptr = 0
        tracking_dict = {}
        right_ptr = 0
        max_length = 0
        
        while right_ptr < len(s):
            tracking_dict[s[right_ptr]] = right_ptr
            right_ptr += 1

            if len(tracking_dict) > 2:
                min_index = min(list(tracking_dict.values()))
                del tracking_dict[s[min_index]]
                min_index += 1 
                left_ptr = min_index
            max_length = max(max_length,right_ptr-left_ptr)
        return max_length
