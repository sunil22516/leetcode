class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        sml=n
        while True:
            prd=1
            for i in str(sml):
                prd= prd*int(i)

            if prd%t ==0:
                return sml
                break
            else:
                sml=sml+1