class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        new_dict={}
        n=len(s)
        res=0
        for ch in s:
            if ch not in new_dict:
                new_dict[ch] = 1
            else:
                new_dict[ch] += 1
        if letter in new_dict:
            for key , value in new_dict.items():
                if key == letter:
                    res= value/n * 100
                    res= math.floor(res)
                    return res
        return 0
            