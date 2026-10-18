class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(i for i in s if i.isalnum()).lower()
        l,r = 0,len(x)-1
        while l < r:
            if x[l] ==x[r]:
                l+=1
                r-=1
            else:
                return False
        return True
