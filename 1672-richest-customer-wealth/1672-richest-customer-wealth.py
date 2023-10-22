class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for inner_list in accounts:
            total=0
            for element in inner_list:
                total += element
                if total >= maxi:
                   maxi = total
                else:
                    continue
        return maxi
        