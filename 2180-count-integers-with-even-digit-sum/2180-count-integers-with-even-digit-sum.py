class Solution:
    def countEven(self, num: int) -> int:
        r=0
        count=0
        for i in range(1,num+1):
            temp = i
            digit_sum=0
            while temp>0:
                r=temp%10
                digit_sum += r
                temp//=10
            if digit_sum % 2 == 0:
                count+=1
        return count
                

        