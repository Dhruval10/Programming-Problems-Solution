class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_nums = []
        even_nums = []
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even_nums.append(A[i])
            else:
                odd_nums.append(A[i])
        
        return even_nums + odd_nums                
