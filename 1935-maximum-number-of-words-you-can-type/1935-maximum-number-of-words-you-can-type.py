class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word_count=0
        broken_count=0
        word=""

        for i in range(0,len(text)):
            if text[i] != ' ':
                word += text[i]
            else:
                word_count += 1
                for j in range(0,len(brokenLetters)):
                    if brokenLetters[j] not in word:
                        continue
                    else:
                        broken_count += 1
                        break
                word=""
        word_count += 1
        for k in range(0,len(brokenLetters)):
            if brokenLetters[k] not in word:
                continue
            else:
                broken_count += 1
                break
        count = word_count - broken_count
        return count
            


        