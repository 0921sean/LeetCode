from typing import List

# # Time complexity: O(n^2)
# class Solution:
#     def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
#         # 목적 time
#         target_time = times[targetFriend]
#         # 시간 순서대로 정렬 ([[3, 10], [1, 5], [2, 6]] -> [[1, 5], [2, 6], [3, 10]])
#         times.sort(key=lambda x: x[0])
        
#         # chairs 초기화 ([0, 0, 0])
#         n = len(times)
#         chairs = [0] * n
        
#         for time in times:
#             for i in range(n):
#                 if time[0] >= chairs[i]:
#                     chairs[i] = time[1]
#                     if time == target_time:
#                         return i
#                     break

# Time complexity: O(nlogn)
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # 이벤트 초기화
        events = []
        
        # 이벤트 추가 ([[1, 4], [2, 3], [4, 6]] -> [[1, 0], [4, -1], [2, 1], [3, -2], [4, 2], [6, -3]])
        for i, time in enumerate(times):
            events.append([time[0], i])
            events.append([time[1], ~i])
            
        # 시간 순서대로 정렬
        events.sort()
        
        # chairs 초기화
        available_chairs = list(range(len(times)))
        occupied_chairs = []
        
        for event in events:
            time, friend = event
            if friend >= 0:
                chair = heapq.heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(occupied_chairs, [times[friend][1], chair])
            else:
                if occupied_chairs[0][0] <= time:
                    _, chair = heapq.heappop(occupied_chairs)
                    heapq.heappush(available_chairs, chair)
                
                    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    time_lists = [[[1, 4], [2, 3], [4, 6]], [[3, 10], [1, 5], [2, 6]], [[4, 6], [1, 3], [2, 4]]]
    targetFriends = [1, 0, 0]
    for time_list, targetFriend in zip(time_lists, targetFriends):
        result = solution.smallestChair(time_list, targetFriend)
        print(result)