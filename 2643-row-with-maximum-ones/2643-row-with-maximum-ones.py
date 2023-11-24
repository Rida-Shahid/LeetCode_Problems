class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index=0
        max_one=0

        for i in range(0,len(mat)):
            count=sum(mat[i])
            if count>max_one:
                max_one = count
                index=i
        return [index,max_one]
            
        
               
                
            



