class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        size=len(words)
        
        

        for word in words:
            for ch in word:
                if ch not in allowed:
                    size=size-1
                    break  #loop should end if first non-allowed char encounter if we dont use break then it will count all the non_allowed chars in the word
                else:
                    continue
        return size
                    
        