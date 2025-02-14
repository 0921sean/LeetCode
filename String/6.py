# # 시간 끝자락
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         div = (numRows - 1) * 2
#         result = ""
        
#         for i in range(div//2 + 1):
#             for x, a in enumerate(s):
#                 if div == 0:
#                     result = s
#                     break
#                 if x % div == i or x % div == div - i:
#                     result += a
                    
#         return result

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]
        
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
            
        for i in range(numRows):
            rows[i] = "".join(rows[i])
            
        return "".join(rows)
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    s_list = ["PAYPALISHIRING", "PAYPALISHIRING", "A"]
    numRows_list = [3,4,1]
    for s, numRows in zip(s_list, numRows_list):
        result = solution.convert(s, numRows)
        print(result)