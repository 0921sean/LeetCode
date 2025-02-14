class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        
        for a in s:
            if a == " ":
                if result != "":
                    break
            elif a == "-" or a == "+":
                if result == "":
                    result += a
                else:
                    break
            elif a.isdigit():
                result += a
            else:
                break
        if result == "" or result == "-" or result == "+":
            return 0
        elif int(result) > 2**31 - 1:
            return 2**31 - 1
        elif int(result) < -2**31:
            return -2**31
        else:
            return int(result)
        
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    s_list = ["42", "   -42", "4193 with words", "words and 987", "-91283472332", "3.14159", "  -0012a42", "+-12", "21474836460", "2147483648", "   +0 123"]
    for s in s_list:
        result = solution.myAtoi(s)
        print(result)