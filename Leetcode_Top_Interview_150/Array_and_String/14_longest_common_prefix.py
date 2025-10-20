from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for letter in strs[0]:
            prefix += letter
            for word in strs:
                if word[:len(prefix)] != prefix:
                    return prefix[:-1]
        
        return prefix