class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        new_str=""
        count=0
        for ch in sentence:
            if ch not in new_str:
                new_str += ch
                count+=1
        if count == 26:
            return True
        else:
            return False

        