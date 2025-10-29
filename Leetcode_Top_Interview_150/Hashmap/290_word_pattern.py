class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        pattern_match = {}
        s_match = {}

        if len(pattern) != len(s_words):
            return False

        for i in range(len(pattern)):
            ch1, ch2 = pattern[i], s_words[i]
            if ch1 not in pattern_match:
                pattern_match[ch1] = []
            pattern_match[ch1].append(i)

            if ch2 not in s_match:
                s_match[ch2] = []
            s_match[ch2].append(i)

        return sorted(pattern_match.values()) == sorted(s_match.values())