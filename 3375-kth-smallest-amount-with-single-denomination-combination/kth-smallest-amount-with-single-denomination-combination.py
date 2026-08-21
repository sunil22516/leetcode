from fractions import gcd
from itertools import combinations

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        subsets = []
        for mask in range(1, 1 << n):
            cur_lcm = 1
            bits = 0
            for i in range(n):
                if mask & (1 << i):
                    cur_lcm = lcm(cur_lcm, coins[i])
                    bits += 1
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((cur_lcm, sign))
        
        def count_le(x):
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (x // lcm_val)
            return total
        
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo