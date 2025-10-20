class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        idx = 0
        result = 0

        while idx < len(s):
            if idx != len(s)-1 and (s[idx], s[idx+1]) in [('I', 'V'), ('I', 'X'), ('X', 'L'), ('X', 'C'), ('C', 'D'), ('C', 'M')]:
                result += rom_to_num[s[idx+1]] - rom_to_num[s[idx]]
                idx += 2
            else:
                result += rom_to_num[s[idx]]
                idx += 1

        return result