class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_dict = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
            'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
            's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
        }
        temp2=[]
        unique=[]
        temp=""
        count=0
        for word in words:
            for i in range(0,len(word)):
                temp += morse_code_dict[word[i]]  
            temp2.append(temp) 
            temp=temp[:0] 
        for item in temp2:
            if item not in unique:
                unique.append(item)
        count=len(unique)
        return count
                






