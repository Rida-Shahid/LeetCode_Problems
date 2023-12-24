class Solution:
    def maxPower(self, s: str) -> int:
        one=""
        two=""
        count=0
        maxx=0
        for i in range(0,len(s)-1):
            one = s[i]
            two = s[i+1]
            if one == two:
                count += 1
            else:
                count=0
            if count >= maxx:
                maxx=count
        return maxx+1
        