class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 변수 초기화
        result = 0
        
        for char in set(s):
            # char가 문자열에서 등장하는 처음과 마지막 인덱스 찾기
            first = s.find(char)
            last = s.rfind(char)
            if last - first > 1: # 두 char 사이에 문자가 존재할 경우
                unique_middle = set(s[first+1:last])
                result += len(unique_middle)
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    s_list = ['aabca', 'adc', 'bbcbaba']
    for s in s_list:
        result = solution.countPalindromicSubsequence(s)
        print(result)