class Solution:
    def removeVowels(self, s: str) -> str:
        for vowel in ["a","e","i","o","u"]:
            s = s.replace(vowel, "")
        return s