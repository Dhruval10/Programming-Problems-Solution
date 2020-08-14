class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        list1 = []
        for i in nums:
            if i in list1:
                list1.remove(i)
            elif i not in list1:
                list1.append(i)
        return list1[0]
