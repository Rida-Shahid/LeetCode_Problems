class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        new_str=""
        count=0
        n=len(pref)
        for word in words:
            if word[:n] == pref:
                count +=1
            else:
                continue
        return count
           

