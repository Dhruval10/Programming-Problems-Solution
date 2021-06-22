class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        merged_key = s.replace('-','')
        new_str = ''
        dash = k
        for i in range(len(merged_key)-1,-1,-1):
            if dash == 0:
                new_str += '-'
                dash = k
            dash -= 1
            new_str += merged_key[i]
        new_str = new_str[::-1].upper()
        return new_str
