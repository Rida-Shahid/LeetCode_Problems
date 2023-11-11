class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[]
        list1=[]
        list2=[]
        nums1.sort()
        nums2.sort()
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                continue
            else:
                list1.append(nums1[i])
        for j in range (0,len(nums2)):
            if nums2[j] in nums1:
                continue
            else:
                list2.append(nums2[j])
        answer.append(list(set(list1)))
        answer.append(list(set(list2)))
        return answer
               
                    
            


        