class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        new_list=[]
        for i in range(0,len(s)):
            new_str=""
            new_set=set()
            new_str = s[i:i+3]
            new_set = set(new_str)
            if len(new_set) == 3:
                count += 1
        return count
            

    

        