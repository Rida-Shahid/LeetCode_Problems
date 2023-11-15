class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_str=""
        temp=0
        new_list=[]

        for i in range(0,len(digits)):
            new_str += str(digits[i])
        temp = int(new_str)
        temp = temp + 1
        new_str = str(temp)
        for j in range(0,len(new_str)):
            new_list.append(int(new_str[j]))
        return new_list

        
