class Solution:
    def intToRoman(self, num: int) -> str:
        res = 'M' * (num // 1000)
        num %= 1000
        
        val = num // 100
        if val == 9:
            res += 'CM'
        elif val == 4:
            res += 'CD'
        else:
            res += 'D' * (val // 5) + 'C' * (val % 5)
        num %= 100
        
        val = num // 10
        if val == 9:
            res += 'XC'
        elif val == 4:
            res += 'XL'
        else:
            res += 'L' * (val // 5) + 'X' * (val % 5)
        num %= 10
        
        if num == 9:
            res += 'IX'
        elif num == 4:
            res += 'IV'
        else:
            res += 'V' * (num // 5) + 'I' * (num % 5)
        return res
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    num_list = [3749, 58, 1994]
    for num in num_list:
        result = solution.intToRoman(num)
        print(result)