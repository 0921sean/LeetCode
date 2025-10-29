class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True