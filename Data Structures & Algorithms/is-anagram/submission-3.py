class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if len is same, obv false if not equal
        if len(s) != len(t):
            return False
        #counter of each string to see each amount of chars in s and t

        sd = {}
        for char in s:
            sd[char] = sd.get(char, 0) + 1
        
        td = {}
        for char in t:
            td[char] = td.get(char, 0) + 1
        return sd == td
