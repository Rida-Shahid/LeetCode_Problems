class Solution:
    def repeatedCharacter(self, s: str) -> str:
        new_set=set()
        for ch in s:
            if ch not in new_set:
                new_set.add(ch)
            else:
                return ch