class Solution:
    def removeDuplicates(self, s: str) -> str:
        result=""
        stack =[]
        for i in range(0,len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
              stack.append(s[i])
            
        result = ''
        while stack:
            result = stack.pop() + result

        return result

        