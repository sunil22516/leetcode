class Solution(object):
    def maxSubarrayLength(self, nums, k):
        d = {}
        l = ans = 0
        for r, x in enumerate(nums):
            d[x] = d.get(x, 0) + 1
            while d[x] > k:
                d[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans