class Solution(object):
    def separateDigits(self, nums):
        b=[]
        for i in nums:
            if i>=10:
                str1=str(i)
                for j in str1:
                    b.append(int(j))
            else:
                b.append(i)
        return b