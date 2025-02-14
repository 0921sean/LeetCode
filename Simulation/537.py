class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_real, num1_imag = int(num1.split("+")[0]), int(num1.split("+")[1].split("i")[0])
        num2_real, num2_imag = int(num2.split("+")[0]), int(num2.split("+")[1].split("i")[0])
                                                            
        result_real = num1_real * num2_real - num1_imag * num2_imag
        result_imag = num1_real * num2_imag + num1_imag * num2_real
        
        return str(result_real) + "+" + str(result_imag) + "i"
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    num1_list = ["1+1i", "1+-1i"]
    num2_list = ["1+1i", "1+-1i"]
    for num1, num2 in zip(num1_list, num2_list):
        result = solution.complexNumberMultiply(num1, num2)
        print(result)