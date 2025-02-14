from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = ""
        changeStarted = False
        
        for x, i in enumerate(num):
            if change[int(i)] > int(i):
                res += str(change[int(i)])
                changeStarted = True
            elif change[int(i)] == int(i):
                res += i
            else:
                if changeStarted:
                    res += num[x:]
                    break
                else:
                    res += i
            
        return res
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    num_list = ["132", "021", "5", "330", "334111", "214010"]
    change_list = [[9,8,5,0,3,6,4,2,6,8],[9,4,3,5,7,2,1,9,0,6],[1,4,7,5,3,2,5,6,9,4],[9,3,6,3,7,3,1,4,5,8],[0,9,2,3,3,2,5,5,5,5],[6,7,9,7,4,0,3,4,4,7]]
    for num, change in zip(num_list, change_list):
        result = solution.maximumNumber(num, change)
        print(result)