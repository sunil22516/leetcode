class Solution(object):
    def getMinDistance(self, nums, target, start):
        

        k1 = len(nums)
        for i in range(len(nums)) :
            if nums[i] == target:
                k1 =min(k1, abs(i-start))

        return k1