class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        rev=""
        for word in words:
            rev = word[::-1]
            if rev == word:
                return rev 
            
        return ""
        