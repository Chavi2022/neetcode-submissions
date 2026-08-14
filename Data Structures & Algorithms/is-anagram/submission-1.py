class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s =sorted(s)
        t = sorted(t)
        c = Counter(s)
        v = Counter(t)
        return c == v
