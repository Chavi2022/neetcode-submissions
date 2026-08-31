class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "".join(x for x in s if x.isalnum()).lower()
        l=0
        r=len(cs)-1
        while l<r:
            if cs[l]==cs[r]:
                l+=1
                r-=1
            else:
                return False
        return True
    