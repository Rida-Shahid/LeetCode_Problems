class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        n=n//2
        a= s[:n]
        b= s[n:]
        a_list=[]
        b_list=[]
        vowel=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(0,len(a)):
            if a[i] in vowel:
                a_list.append(a[i])
            if b[i] in vowel:
                b_list.append(b[i])
        if len(a_list) == len(b_list):
            return True
        else:
            return False


        