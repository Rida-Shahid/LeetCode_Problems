class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        new_list=[]
        maxi=0
        

        for i in range(0,len(prices)):
            temp = prices[i]
            discount_found = False

            for j in range(i+1,len(prices)):
                disc=prices[j]
                if disc <= temp:
                    new_list.append(temp-disc)
                    discount_found = True
                    break
            if not discount_found:
                new_list.append(temp)   
        return new_list

        