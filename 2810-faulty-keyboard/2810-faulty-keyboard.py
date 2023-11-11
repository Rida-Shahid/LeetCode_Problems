class Solution:
    def finalString(self, s: str) -> str:
        new_str=""
        new_str2=""

        for i in range(0,len(s)):
            if s[i] != 'i':
                new_str += s[i]
            else:
                new_str = new_str[::-1]
        return new_str
        