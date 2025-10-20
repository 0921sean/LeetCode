from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            # Step 1: 현재 줄에 단어를 몇 개 넣을 수 있는지 확인
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # Step 2: 단어들을 line으로 구성
            line_words = words[i:j]
            num_words = j - i
            num_spaces = maxWidth - sum(len(word) for word in line_words)

            # Step 3: 마지막 줄이거나 단어가 한 개뿐이면 left-justify
            if j == len(words) or num_words == 1:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # fully-justify
                space_between = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)

                line = ''
                for k in range(num_words - 1):
                    line += line_words[k]
                    line += ' ' * (space_between + (1 if k < extra_spaces else 0))
                line += line_words[-1]  # 마지막 단어는 공백 뒤에 있음

            result.append(line)
            i = j

        return result

        # 이런 식으로 해보려 했음
        # words_with_len = []
        # for word in words:
        #     words_with_len.append((len(word), word))
        # start, end = 0, 0  # 해당줄의 시작 단어, 해당줄의 끝 단어 인덱스
        # length, count = 0, 0    # 해당줄의 길이, 해당줄에 포함된 단어 개수
        # space_list = [] # ' ' 개수
        # result = []

        # while end < len(words_with_len):
        #     word_len = words_with_len[end][0]
        #     if length + word_len + count <= maxWidth:
        #         length += word_len
        #         count += 1
        #         end += 1
        #     else:
        #         space = (maxWidth - length) // (count - 1)
        #         more_spaces = maxWidth - length - space * count
        #         space_list = [space * count]
        #         for more_space in more_spaces:

        #         line += 
        #         result.append()
        #         start = end
        #         length, count = word_len, 1

        # return result