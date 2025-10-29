class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_match = {}
        t_match = {}

        for i in range(len(s)):
            if s[i] not in s_match:
                s_match[s[i]] = []
            s_match[s[i]].append(i)

            if t[i] not in t_match:
                t_match[t[i]] = []
            t_match[t[i]].append(i)

        return sorted(s_match.values()) == sorted(t_match.values())