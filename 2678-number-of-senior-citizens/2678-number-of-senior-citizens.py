class Solution:
    def countSeniors(self, details: List[str]) -> int:
         
        age=60
        count=0
        num=0
        new_str=""

        for element in details:
            new_str = element[11:13]
            num = int(new_str)
            if num > age:
                count+=1
        return count



        