class Solution:
    def isValid(self, s: str) -> bool:
        if 'abc' in s:
            return self.isValid(s.replace('abc', ''))
        if s == '':
            return True
        return False
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    s_list = ['aabcbc', 'abcabcababcc', 'abccba']
    for s in s_list:
        result = solution.isValid(s)
        print(result)