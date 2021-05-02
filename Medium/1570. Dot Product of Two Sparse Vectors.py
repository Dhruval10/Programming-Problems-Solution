class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict1 = collections.defaultdict(int)
        
        for i in range(len(nums)):
            if nums[i] != 0:
                self.dict1[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        
        for key, value in self.dict1.items():
            if key in vec.dict1:
                result += vec.dict1[key] * value
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
