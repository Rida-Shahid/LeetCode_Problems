class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        new_str=""
        new_str2=""
        count =0



        for i in range(0,len(words)):
            new_str = words[i]
            new_str2 = new_str[::-1]
            if new_str == new_str2:
                count=count-1
            for j in range(0,len(words)):
                if words[j] == new_str2:
                    count += 1
        count=count/2
        return int(count)
                


        