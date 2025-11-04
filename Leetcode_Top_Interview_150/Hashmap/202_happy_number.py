class Solution:
    def isHappy(self, n: int) -> bool:
        process = set()
        
        while n not in process:
            process.add(n)
            digits = [int(d) for d in str(n)]
            n = sum(digit**2 for digit in digits)

        return n == 1