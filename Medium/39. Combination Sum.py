class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def backtracking(path, target, index):
            if target == 0:
                answer.append(path)
                return
            if target < 0:
                return
            for i in range(index,len(candidates)):
                backtracking(path+[candidates[i]],target-candidates[i],i)
        backtracking([],target,0)
        return answer
