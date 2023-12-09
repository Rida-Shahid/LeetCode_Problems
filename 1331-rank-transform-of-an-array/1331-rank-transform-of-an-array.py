class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_arr = list(arr)
        new_list=[]
        dict1={}
        temp=0
        sort_arr = sorted(set(sort_arr))
        for i in range(0,len(sort_arr)):
            dict1[sort_arr[i]] = i+1
        for j in arr:
            temp = dict1[j]
            new_list.append(temp)
        return new_list
            