# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         n = len(senate)
#         i = -1
        
#         while 'R' in senate and 'D' in senate:
#             found = False
#             i += 1
#             if i >= n:
#                 i = 0
                
#             if senate[i] == 'R':
#                 for j in range(i+1, n):
#                     if senate[j] == 'D':
#                         senate = senate[:j] + senate[j+1:]
#                         n -= 1
#                         found = True
#                         break
#                 if not found:
#                     for j in range(0, i):
#                         if senate[j] == 'D':
#                             senate = senate[:j] + senate[j+1:]
#                             n -= 1
#                             i -= 1
#                             break
#             elif senate[i] == 'D':
#                 for j in range(i+1, n):
#                     if senate[j] == 'R':
#                         senate = senate[:j] + senate[j+1:]
#                         n -= 1
#                         found = True
#                         break
#                 if not found:
#                     for j in range(0, i):
#                         if senate[j] == 'R':
#                             senate = senate[:j] + senate[j+1:]
#                             n -= 1
#                             i -= 1
#                             break
            
#         if 'R' not in senate:
#             return "Dire"
#         if 'D' not in senate:
#             return "Radiant"
        
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        i = 0
        
        while 'R' in senate and 'D' in senate:
            found = False
            target = 'R' if senate[i] == 'D' else 'D'
            for j in range(i+1, len(senate)):
                if senate[j] == target:
                    senate.pop(j)
                    found = True
                    break
            if not found:
                for j in range(i):
                    if senate[j] == target:
                        senate.pop(j)
                        i -= 1
                        break
            i += 1
            if i >= len(senate):
                i = 0
            
        if 'R' not in senate:
            return "Dire"
        if 'D' not in senate:
            return "Radiant"
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    senate_list = ["RD", "RDD", "DDRRR", "DRRDRD", "DDDRRRRR"]
    for senate in senate_list:
        result = solution.predictPartyVictory(senate)
        print(result)