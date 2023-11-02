class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        size_arr=len(words)
        st=""
        for i in range(0,size_arr):
            st += words[i][0] 
        if(s==st):
            return True
        else:
            return False



        