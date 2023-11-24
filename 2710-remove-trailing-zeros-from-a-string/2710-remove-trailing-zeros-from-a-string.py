class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n=len(num)-1

        for i in range(n,-1,-1):
            if num[i] == '0':
                continue
            else:
                return num[0:i+1]
        return num
        