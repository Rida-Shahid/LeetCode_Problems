
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                summ = nums1[i][1] + nums2[j][1]
                id1 = nums1[i][0]
                temp = [id1, summ]
                res.append(temp)
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        # Append remaining elements from nums1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        # Append remaining elements from nums2
        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res
