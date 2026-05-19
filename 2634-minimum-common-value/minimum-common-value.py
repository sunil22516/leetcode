class Solution(object):
    def getCommon(self, nums1, nums2):
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                return nums1[i]
            else:
                if nums1[i]>nums2[j]:
                    j=j+1
                else:
                    i=i+1
        return -1