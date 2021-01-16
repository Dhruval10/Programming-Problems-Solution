class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        len1 = len(version1)
        len2 = len(version2)
        
        if len1 < len2:
            for i in range(len2 - len1):
                version1 += '0'
        elif len1 > len2:
            for j in range(len1 - len2):
                version2 += "0"
        
        for i in range(max(len1,len2)):
            if int(version1[i]) < int(version2[i]):
                return -1
            elif int(version1[i]) > int(version2[i]):
                return 1
            else:
                pass
        return 0