class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_i = 0
        t_i = 0
        str1 = ''
        if len(s)  == 0:
            return True
        else:
            while(s_i < len(s) and t_i < len(t)):
                if s[s_i] == t[t_i]:
                    str1 += s[s_i]
                    s_i += 1
                    t_i += 1
                else:
                    t_i += 1
            return str1 == s
