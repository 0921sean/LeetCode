class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factorization(n):
            factors = []
            i = 2
            while i * i <= n:  # √n까지 탐색
                while n % i == 0:
                    factors.append(i)
                    n //= i
                i += 1
            if n > 1:
                factors.append(n)  # 마지막 소수 추가
            return sum(factors)
        
        while True:
            new_n = prime_factorization(n)
            if new_n == n:
                break
            n = new_n
            
        return n
        
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    n_list = [15, 3]
    for n in n_list:
        result = solution.smallestValue(n)
        print(result)