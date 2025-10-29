from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            if word not in anagrams:
                anagrams[word] = []
            anagrams[word].append(strs[i])
        
        return list(anagrams.values())