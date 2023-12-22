class Solution:
    def maxScore(self, s: str) -> int:
        left=""
        right=""
        n=len(s)
        count=0
        maxx=0
        for i in range(1,n):
            count=0
            left = s[0:i]
            right= s[i:n]
            for j in left:
                if j == '0':
                    count += 1
            for k in right:
                if k == '1':
                    count += 1
            if count >= maxx:
                maxx = count     
        return maxx
                



        