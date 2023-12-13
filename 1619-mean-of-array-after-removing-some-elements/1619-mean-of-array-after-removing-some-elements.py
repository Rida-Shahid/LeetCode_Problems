class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        max5 = int(5/100 * n)
        min5= int(5/100 * n)
        div = n-min5-max5
        summ=0
        mean=0
        summ += sum(arr[min5:n-max5])
        mean = float(summ/div)
        return mean

        