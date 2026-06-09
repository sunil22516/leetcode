class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        o = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                o += cost[i]
        return o
        