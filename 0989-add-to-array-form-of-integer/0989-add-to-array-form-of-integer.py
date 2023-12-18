import sys
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ""
        num_int = 0
        add=""
        res=[]
        sys.set_int_max_str_digits(100000)
        for i in range(0,len(num)):
            num_str += str(num[i])
        num_int = int(num_str)
        add = str(num_int + k)
        for j in range(0,len(add)):
            res.append(int(add[j]))
        return res
