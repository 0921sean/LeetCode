class Solution:
    def clumsy(self, n: int) -> int:
        result = 0
        add_or_sub = 1
        for i in range(n, -1, -4):
            if i == 3:
                return (result + add_or_sub * 6)
            if i == 2:
                return (result + add_or_sub * 2)
            if i == 1:
                return (result + add_or_sub * 1)
            if i == 0:
                return result
            result += add_or_sub * (i * (i-1) // (i-2))
            result += (i-3)
            add_or_sub = -1
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    n_list = [4, 10]
    for n in n_list:
        result = solution.clumsy(n)
        print(result)