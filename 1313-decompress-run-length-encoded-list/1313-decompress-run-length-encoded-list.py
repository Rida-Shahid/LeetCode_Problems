'''class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        temp=[]
        sublist=[]
        decomp=[]
        for i in nums:
            temp.append(i)
            if (len(temp)==2):
                for i in temp: 
                    sublist.append(i)
                first = int(sublist[0])
                for i in range(0,first):
                    decomp.append(sublist[1])
                temp.clear()
                sublist.clear()
            else:
                continue
        return decomp '''
                
# without using sublist because it was extra 

class Solution:       
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        temp=[]
        decomp=[]
        for i in nums:
            temp.append(i)
            if (len(temp)==2):
                first = int(temp[0])
                for i in range(0,first):
                    decomp.append(temp[1])
                temp.clear()
                
            else:
                continue
        return decomp
                


        