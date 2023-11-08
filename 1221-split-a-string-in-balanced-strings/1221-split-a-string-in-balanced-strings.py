class Solution:
    def balancedStringSplit(self, s: str) -> int:

        r_count=0
        l_count=0
        ss_count=0
        new_str=""

        for ch in s:
            new_str=""
            if ch == 'R':
                new_str += ch
                r_count += 1
            elif ch == 'L':
                new_str += ch
                l_count += 1
            if (r_count == l_count):
                ss_count += 1
        return ss_count


    
        