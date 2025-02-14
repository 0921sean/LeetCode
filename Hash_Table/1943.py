from typing import List

# # Example 3의 경우, 합은 같은데 color sets가 달라서 구분해야 하는 경우를 하기 어려움.
# class Solution:
#     def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
#         # 변수값 초기화
#         painting_list = [0] * 100001
#         max_time = 0
        
#         # painting_list = [0, 14, 14, 14, 16, 16, 16, 0, 0, ...]
#         for segment in segments:
#             start, end, value = segment
#             for i in range(start, end):
#                 painting_list[i] += value
#             max_time = max(max_time, end)
                
#         result = []
#         start = None
#         for i in range(max_time + 1):
#             # 처음 14를 만나면 start = 1
#             if painting_list[i] > 0:
#                 if start is None:
#                     start = i
#                 elif start is not None and painting_list[i] != painting_list[i - 1]:
#                     result.append([start, i, painting_list[start]])
#                     start = i  
#             else:
#                 if start is not None:
#                     result.append([start, i, painting_list[start]])
#                     start = None
            
#         return result
    
# Memory Limit Exceeded Error
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # 변수값 초기화
        painting_list = [set() for _ in range(100001)]
        max_time = 0
        
        # painting_list = [0, 14, 14, 14, 16, 16, 16, 0, 0, ...]
        for segment in segments:
            start, end, value = segment
            for i in range(start, end):
                painting_list[i].add(value)
            max_time = max(max_time, end)
            
        result = []
        start = None
        prev = None
        for i in range(max_time + 1):
            current = painting_list[i]
                
            if current:
                if start is None:
                    start = i
                elif start is not None and current != prev:
                    result.append([start, i, sum(prev)])
                    start = i
                prev = current
            else:
                if start is not None:
                    result.append([start, i, sum(prev)])
                    start = None
            
        return result

# Time complexity: O(nlogn)
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)
        
        for start, end, color in segments:
            events[start] += color
            events[end] -= color
            
        result = []
        prev, color = None, 0
        for current in sorted(events):
            if color: # if color == 0, 그 부분이 합 0임을 의미
                result.append([prev, current, color])
            
            color += events[current]
            prev = current
            
        return result

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    segment_lists = [[[1,4,5],[4,7,7],[1,7,9]], [[1,7,9],[6,8,15],[8,10,7]], [[1,4,5],[1,4,7],[4,7,1],[4,7,11]], [[4,16,12],[9,10,15],[18,19,13],[3,13,20],[12,16,3],[2,10,10],[3,11,4],[13,16,6]]]
    for segment in segment_lists:
        result = solution.splitPainting(segment)
        print(result)