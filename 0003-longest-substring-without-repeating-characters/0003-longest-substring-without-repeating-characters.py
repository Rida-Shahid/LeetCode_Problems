class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        size=len(s) 
        for i in range(0,size):
           new_str=""
           for j in range (i,size):
                if s[j] not in new_str:
                   new_str += s[j]
                   length=max(length,len(new_str))
                else:
                    break
        return length

