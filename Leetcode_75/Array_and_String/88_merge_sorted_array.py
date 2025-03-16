from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
                # print("nums1 added:", nums1_save)
                # print("i, j:", i, j)
            else:
                result.append(nums2[j])
                j += 1
                # print("nums2 added:", nums1_save)
                # print("i, j:", i, j)
                
        result.extend(nums1[i:m])
        result.extend(nums2[j:n])
        
        for k in range(m + n):
            nums1[k] = result[k]
        return nums1
        
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums1_list = [[1,2,3,0,0,0], [1], [0]]
    m_list = [3, 1, 0]
    nums2_list = [[2,5,6], [], [1]]
    n_list = [3, 0, 1]
    for nums1, m, nums2, n in zip(nums1_list, m_list, nums2_list, n_list):
        result = solution.merge(nums1, m, nums2, n)
        print(result)