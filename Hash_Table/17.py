from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        
        for digit in digits:
            if not result:
                result = [i for i in dict[digit]]
            else:
                temp = result.copy()
                result = []
                for i in temp:
                    for j in dict[digit]:
                        result.append(i + j)
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    digits_list = ["23", "", "2"]
    for digits in digits_list:
        result = solution.letterCombinations(digits)
        print(result)