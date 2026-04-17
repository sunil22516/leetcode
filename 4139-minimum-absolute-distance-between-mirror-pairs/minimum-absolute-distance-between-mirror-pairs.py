class Solution(object):
    def minMirrorPairDistance(self, nums):
        def reverse(x):
            return int(str(x)[::-1])
        
        last_seen = {}   # stores reverse(nums[i]) -> index i
        ans = float('inf')
        
        for j in range(len(nums)):
            
            if nums[j] in last_seen:
                ans = min(ans, j - last_seen[nums[j]])
            
            # store reverse of current
            rev = reverse(nums[j])
            last_seen[rev] = j
        
        return ans if ans != float('inf') else -1