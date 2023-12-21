class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        index = n  # Initialize index to the end of the string

        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                index = i
            elif s[i] == 'b' and index < n:
                return False

        return True
