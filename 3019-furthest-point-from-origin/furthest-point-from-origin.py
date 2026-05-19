class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        L=0
        R=0
        D=0
        for i in moves:
            if i=="R":
                R=R+1
            if i=="L":
                L=L+1
            if i=="_":
                D=D+1
        return abs(R-L)+D



        