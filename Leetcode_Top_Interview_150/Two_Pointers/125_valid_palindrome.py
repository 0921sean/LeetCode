class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_word = ''

        for a in s:
            if a.isalpha():
                check_word += a.lower()
            if a.isdigit():
                check_word += a
        
        for i in range(len(check_word) // 2):
            if check_word[i] != check_word[len(check_word) - i - 1]:
                return False

        return True