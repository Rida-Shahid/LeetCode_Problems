class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length=len(sentences)
        maxi=0
        for sentence in sentences:
            count=0
            for ch in sentence:
                if(ch == " "):
                    count=count+1
                else:
                    continue
                if count>maxi:
                    maxi=count
                else:
                    continue
            
        return maxi+1

        