class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        res=""
        palindrom=""
        abc = set('abcdefghijklmnopqrstuvwxyz0123456789')
        for i in range(0,len(s)):
            if s[i] in abc:
                res += s[i]
        #palindrom = res[::-1]
        return res == res[::-1]
