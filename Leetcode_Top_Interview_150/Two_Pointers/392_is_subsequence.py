class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True
            
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
            
            if i == len(s):
                return True
        if i != len(s):
            return False