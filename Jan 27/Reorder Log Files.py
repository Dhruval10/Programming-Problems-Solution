class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        numberList = []
        stringList = []
        
        for log in logs:
            answer = log.split()
            if answer[1].isdigit():
                numberList.append(log)
            else:
                stringList.append(log)
        
        stringList = sorted(stringList, key = lambda x: x.split()[0])
        stringList = sorted(stringList, key = lambda x: x.split()[1:])
        
        return stringList+numberList
