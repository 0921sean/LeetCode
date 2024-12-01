class Solution:
    def clearDigits(self, s: str) -> str:
        list = []
        for a in s:
            if a.isdigit():
                list.pop()
            else:
                list.append(a)

        result = ''
        for a in list:
            result += a
        return result
    
# 실행 예시
if __name__ == "__main__":
    solution = Solution()
    test_string = "a1bc2d3"
    result = solution.clearDigits(test_string)
    print(result)  # 예상 결과: "bd"