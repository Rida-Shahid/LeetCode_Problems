class Solution:
    def reverseWords(self, s: str) -> str:
        new_str=""
        word=""
        
        for i in range(0,len(s)):
            if s[i] != " ":
                word += s[i]
               
            elif s[i] == " ":
                new_str += word[::-1] + " "
                word=""
        new_str += word[::-1]       
        return new_str
        