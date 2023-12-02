class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        new_dict={}
        for char in s:
            if char not in new_dict:
                new_dict[char]  = 1
            else:
                new_dict[char]  +=1
        new_set = set(new_dict.values())
        if len(new_set) == 1:
            return True
        else:
            return False
        