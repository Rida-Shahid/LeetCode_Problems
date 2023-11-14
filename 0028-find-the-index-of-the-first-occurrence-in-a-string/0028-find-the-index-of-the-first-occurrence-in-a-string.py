class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        found=False
        size=len(haystack)
        index=-1
    
        for i in range(size - n + 1):
            if haystack[i:n] == needle:
               index = i
               found= True
               break
            i += n-1
            n=n+1
           
        if found == True:
            return index
        else:
            return -1

        
            
        