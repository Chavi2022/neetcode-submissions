class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1
        l = 0
        ss = ''.join(filter(str.isalnum, s)).lower()
        return ss == ss[::-1]
