class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for element in words:
            size=len(element)
            for i in range(0,size):
                if element == s[:i+1]:
                    count+=1
        return count
             

        
        