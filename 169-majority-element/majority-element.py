class Solution(object):
    def majorityElement(self, nums):
        count = 0
        c = None

        for num in nums:
            if count == 0:
                c = num

            if num == c:
                count += 1
            else:
                count -= 1

        return c