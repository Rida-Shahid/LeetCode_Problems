class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique={}
        n=len(unique)
        for element in arr:
            if element not in unique:   #{(1,3).(2.2).(3.1)}
                unique[element] = 1     #{(1,1),(2,1)} len=2
            else:
                unique[element] += 1
        new_set=set(unique.values()) #(3,2,1)
        if len(unique) == len(new_set):  #len=3
            return True
        else:
            return False
        
        


        