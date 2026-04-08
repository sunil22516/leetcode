class Solution(object):
    def xorAfterQueries(self, nums, queries):
        m = 10**9 + 7
        
        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % m
                i += k
        
        x = 0
        for num in nums:
            x ^= num
        
        return x
        