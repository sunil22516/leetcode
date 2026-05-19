class Solution(object):
    def isGood(self, nums):
        if len(nums)==0:
            return False
        else:
            b=[]
            for i in range(1,max(nums)+1):
                b.append(i)
            b.append(max(nums))
            if sorted(nums)==sorted(b):
                return True
            else:
                False
        return False
        