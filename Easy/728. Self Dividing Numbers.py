class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        answer = []
        
        for number in range(left, right+1):
            temp_num = number
            list1 = []
            while number > 0:
                list1.append(number%10)
                number = number // 10
            is_divided = True
            if 0 in list1:
                continue
            for i in range(len(list1)):
                if temp_num % list1[i] != 0:
                    is_divided = False
            if is_divided == True:
                answer.append(temp_num)
        return answer
