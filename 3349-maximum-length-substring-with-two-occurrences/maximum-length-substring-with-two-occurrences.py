class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxlen=0
        for i in range(len(s)):
            l1=""
            l2=""
            newmaxlen=0
            for j in range(i,len(s)):
                if s[j] in l1 and s[j] in l2:
                    break
                else:
                    if s[j] in l1:
                        l2=l2+s[j]
                        newmaxlen=newmaxlen+1
                    else:
                        l1=l1+s[j]
                        newmaxlen=newmaxlen+1
            maxlen=max(newmaxlen,maxlen)
        return maxlen