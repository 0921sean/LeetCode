class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # 1. 딕셔너리 활용
        # count_dict = {}
        
        # for alp in s:
        #     if alp not in count_dict.keys():
        #         count_dict[alp] = 1
        #     count_dict[alp] += 1
            
        # count_set = set(count_dict.values())
        # if len(count_set) == 1:
        #     return True
        # return False
    
        # 2. 알파벳이 26개임을 활용
        # count_list = [0] * 26
        
        # for alp in s:
        #     count_list[ord(alp) - ord('a')] += 1
        
        # count_list = list(filter(lambda x: x != 0, count_list))
        # count_set = set(count_list)
        # if len(count_set) == 1:
        #     return True
        # return False
        
        # 3. 딕셔너리 활용 방식이나 문자의 개수들을 확인할 때 방법을 변경
        count_dict = {}
        
        for alp in s:
            if alp in count_dict:
                count_dict[alp] += 1
            else:
                count_dict[alp] = 1
                
        isTrue = True
        first = count_dict[s[0]]
        
        for val in count_dict.values():
            if val != first:
                isTrue = False
                break
            
        return isTrue
    
if __name__ == "__main__":
    solution = Solution()
    s_list = ["abacbc", "aaabb"]
    for s in s_list:
        result = solution.areOccurrencesEqual(s)
        print(result)