class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count=0
        temp=0
        
        for i in range(0,len(s)):  
            if s[i] != ' ':
                count += 1
                temp = count
            else:
                count = 0  
        return temp

        