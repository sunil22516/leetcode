class Solution(object):
    def judgeCircle(self, moves):
        a=b=0
        i=0
        n=len(moves)
        while i<n:
            c=moves[i]
            if c=='U': b+=1
            elif c=='D': b-=1
            elif c=='R': a+=1
            else: a-=1
            i+=1
        return a==0 and b==0