class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        non = ''.join(filter(str.isalnum,s)).lower()
        return non == non[::-1]
