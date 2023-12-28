class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the strings to easily find the common prefix
        strs.sort()

        # Take the first and last strings (after sorting)
        first_string = strs[0]
        last_string = strs[-1]

        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(len(first_string)):
            if i < len(last_string) and first_string[i] == last_string[i]:
                common_prefix.append(first_string[i])
            else:
                break

        return "".join(common_prefix)





        

        