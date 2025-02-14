from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # 초기화
        output_list = []
        checked = 1
        
        for i in range(1, n+1):
            if i in target:
                while checked != i:
                    output_list.append("Push")
                    output_list.append("Pop")
                    checked += 1
                output_list.append("Push")
                checked += 1
                
        return output_list
                
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    target_list = [[1, 3], [1, 2, 3], [1, 2]]
    n_list = [3, 3, 4]
    for target, n in zip(target_list, n_list):
        result = solution.buildArray(target, n)
        print(result)