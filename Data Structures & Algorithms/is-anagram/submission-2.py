class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        setS = {}
        for char in s:
            if char in setS:
                setS[char] += 1
            else:
                setS[char] =1
        setT = {}
        for char in t:
            if char in setT:
                setT[char] += 1
            else:
                setT[char] =1
        return setS == setT
