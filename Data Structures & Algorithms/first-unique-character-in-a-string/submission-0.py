class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)
        for i,c in enumerate(s):
            if x[c] == 1:
                return i
        return -1