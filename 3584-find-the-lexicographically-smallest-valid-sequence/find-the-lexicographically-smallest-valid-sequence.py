class Solution:
    def validSequence(self, a: str, b: str) -> List[int]:
        n,m=len(a),len(b)
        s=[0]*(n+1)
        j=m-1
        for i in range(n-1,-1,-1):
            s[i]=s[i+1]
            if j>=0 and a[i]==b[j]:
                s[i]=s[i+1]+1;j-=1

        ans=[];p=-1;bad=0
        for j,c in enumerate(b):
            i=p+1
            if i<n and (a[i]==c or (not bad and s[i+1]>=m-j-1)):
                bad+=a[i]!=c;ans.append(i);p=i;continue
            while i<n and a[i]!=c:i+=1
            if i==n:return []
            ans.append(i);p=i
        return ans