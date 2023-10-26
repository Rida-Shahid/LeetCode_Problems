class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[]
        arr = [first]
        x= arr[0]
        for i in range(len(encoded)):
            x = (x ^ encoded[i])
            arr.append(x)     
        return arr

        #Yayyy!!


        