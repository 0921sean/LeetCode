from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = Counter(words) # words 리스트에서 각각의 개수를 dict 형식으로 등록해주는 함수
        num_words = len(words)
        total_len = word_len * num_words
        result = []

        for i in range(word_len):
            left = i
            curr_count = Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    curr_count[word] += 1
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                    if j + word_len - left == total_len:
                        result.append(left)
                else:
                    curr_count.clear()
                    left = j + word_len

        return result