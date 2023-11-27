class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        new_list=[]
        dist={}
        for s in arr:
            if s not in dist:
                dist[s] = 1
            else:
                dist[s] +=1
        for key,value in dist.items():
            if value == 1:
                new_list.append(key)
        if len(new_list) < k:
            return ""
        else:
            k=k-1
            return new_list[k]


        