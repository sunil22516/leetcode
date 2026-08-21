class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        count = {}
        for i in range(n - k + 1):
            window = set(nums[i:i+k])  # unique values in this window
            for num in window:
                count[num] = count.get(num, 0) + 1

        candidates = [num for num, c in count.items() if c == 1]
        return max(candidates) if candidates else -1