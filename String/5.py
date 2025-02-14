# # Time 완전 끝자락
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         substring_list = []
#         max_len = 0
        
#         for left in range(n):
#             for right in range(n, left, -1):
#                 if s[left:right] == s[left:right][::-1]:
#                     substring_list.append(s[left:right])
                    
#         # print(substring_list)
        
#         for substring in substring_list:
#             if len(substring) > max_len:
#                 max_len = len(substring)
#                 result = substring
                
#         return result

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        substring_list = []
        max_len = 0
        
        for left in range(n):
            for right in range(n, left+1, -1):
                if s[right-1] == s[left] and s[left:right] == s[left:right][::-1]:
                    substring_list.append(s[left:right])
                    
        # print(substring_list)
        
        if substring_list == []:
            return s[0]
                    
        for substring in substring_list:
            if len(substring) > max_len:
                max_len = len(substring)
                result = substring
                
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    s_list = ["babad", "cbbd"]
    for s in s_list:
        result = solution.longestPalindrome(s)
        print(result)