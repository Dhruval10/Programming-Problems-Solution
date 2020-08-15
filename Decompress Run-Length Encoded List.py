class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list1 = []
        lent = int(len(nums))
        
        for i in range(0,lent,2):
            temp_list = []
            for j in range(nums[i]):
                temp_list.append(nums[i+1])
            list1 += temp_list
        del temp_list
        return list1
