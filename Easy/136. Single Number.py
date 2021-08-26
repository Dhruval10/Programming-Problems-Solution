class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        multiple = set()
        single = set()
        
        for num in nums:
            if num not in single and num not in multiple:
                single.add(num)
            else:
                single.remove(num)
                multiple.add(num)
        
        return list(single)[0]
