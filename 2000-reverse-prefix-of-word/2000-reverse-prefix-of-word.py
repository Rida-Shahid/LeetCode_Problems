class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=""
        for i in range(0,len(word)):
            if word[i] == ch:
                s = word[i::-1] + word[i+1:] 
                break
            elif ch not in word:
                return word
        return s
        



        