from typing import List

# # 시간 효율 매우 낮음
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         store_dict = {} # Key: substring, Value: length
#         temp = {}   # Swap을 위한 변수
#         max_len = 0 # 최대 길이
#         for alpha in s:
#             temp = store_dict.copy()
            
#             # 최대 길이 갱신
#             if max(store_dict.values(), default=0) > max_len:
#                 max_len = max(store_dict.values(), default=0)
                
#             # Ex) 'dvdk'
#             # {'d': 1} -> {'dv': 2, 'v': 1} / {'dv': 2, 'v': 1} -> {'vd': 2, 'd': 1}
#             for key, value in store_dict.items():
#                 if alpha not in key:
#                     temp[key + alpha] = value + 1
#                 del temp[key]
#             temp[alpha] = 1
#             store_dict = temp
            
#         return max(max_len, max(store_dict.values(), default=0))

# # 시간 효율 매우 낮음
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         store_dict = {}
#         temp = {}
#         for alpha in s:
#             temp = store_dict.copy()
            
#             for key, value in store_dict.items():
#                 if value == True:
#                     if alpha not in key:
#                         temp[key + alpha] = True
#                     temp[key] = False
#             temp[alpha] = True
#             store_dict = temp
#         return max((len(key) for key in store_dict.keys()), default=0)
            
# # O(n) 풀이 (답지 봄)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = max_len = 0
#         char_set = set()
        
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
                
#             char_set.add(s[right])
#             max_len = max(max_len, right - left + 1)
            
#         return max_len
    
# O(n) 풀이 (답지 봄)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        count = {}
        
        for right, c in enumerate(s):
        	# count dict의 key: 문자, value: 개수
            count[c] = 1 + count.get(c, 0)
            # 중복 문자가 있을 경우 left 포인터 이동 (중복 문자가 없을 때까지)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
                
            # 최대 길이 갱신
            max_len = max(max_len, right - left + 1)
            
        return max_len

# # O(n) 풀이 (답지 봄)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = max_len = 0
#         last_seen = {}
        
#         for right, c in enumerate(s):
#             if c in last_seen and last_seen[c] >= left:
#                 left = last_seen[c] + 1
                
#             max_len = max(max_len, right - left + 1)
#             last_seen[c] = right
            
#         return max_len
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    str_list = ["abcabcbb", "bbbbb", "pwwkew", " ", "", "   ", "dvdf", "dvdf d   a"]
    for str in str_list:
        result = solution.lengthOfLongestSubstring(str)
        print(result)