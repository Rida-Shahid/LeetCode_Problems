class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count=0
        new_str=""
        for i in s:
            new_str= new_str + str(i)
            if(i==" "):
                count=count+1
            else:
                continue
            if (count==k):
                new_str = new_str[:-1]
                break
        return new_str
        
           

        