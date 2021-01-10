class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        cnt1 = 0
        cnt2 = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        while cnt1<len(nums1) and cnt2<len(nums2):
            if nums1[cnt1] == nums2[cnt2]:
                ans.append(nums1[cnt1])
                cnt1 += 1
                cnt2 += 1
            elif nums1[cnt1] > nums2[cnt2]:
                cnt2 += 1
            elif nums1[cnt1] < nums2[cnt2]:
                cnt1 += 1
        return ans