class Solution(object):
    def longestSubsequence(self, nums):
        t=0
        zero=True
        l1=nums
        for i in nums:
            t^=i
            if i!=0:
                zero=False
        if t!=0:
            return len(nums)
        if not zero:
            return len(nums)-1
        return 0
        
        