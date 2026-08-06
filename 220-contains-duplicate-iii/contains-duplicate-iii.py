class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        w = valueDiff + 1
        for i, n in enumerate(nums):
            b = n // w
            if b in buckets or (b-1 in buckets and n-buckets[b-1]<=valueDiff) or (b+1 in buckets and buckets[b+1]-n<=valueDiff):
                return True
            buckets[b] = n
            if i >= indexDiff:
                del buckets[nums[i-indexDiff] // w]
        return False