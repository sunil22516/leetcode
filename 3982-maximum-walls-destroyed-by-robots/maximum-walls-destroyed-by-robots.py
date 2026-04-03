from bisect import bisect_left, bisect_right

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        n = len(robots)

        # Sort robots by position, keeping distances paired
        order = sorted(range(n), key=lambda i: robots[i])
        pos  = [robots[i]   for i in order]
        dist = [distance[i] for i in order]

        sw       = sorted(walls)
        wall_set = set(walls)

        def count(lo, hi):
            if lo > hi:
                return 0
            return bisect_right(sw, hi) - bisect_left(sw, lo)

        # Walls sitting exactly on a robot are always destroyed (free, direction-independent)
        auto = sum(1 for p in pos if p in wall_set)

        # Walls beyond the two ends — only reachable by the edge robots
        left_outer  = count(pos[0]  - dist[0],  pos[0]  - 1)
        right_outer = count(pos[-1] + 1,        pos[-1] + dist[-1])

        # DP over sorted robots
        # dp_left  = best wall count if current robot fires LEFT
        # dp_right = best wall count if current robot fires RIGHT
        dp_left  = left_outer   # robot 0 fires left  → captures left_outer
        dp_right = 0            # robot 0 fires right → nothing to its left

        for i in range(n - 1):
            lo, hi = pos[i], pos[i + 1]

            # Walls in open gap (lo, hi) each side can reach
            r_count = count(lo + 1,                         min(lo + dist[i],     hi - 1))
            l_count = count(max(hi - dist[i + 1], lo + 1),                        hi - 1)
            inter   = count(max(hi - dist[i + 1], lo + 1), min(lo + dist[i],     hi - 1))
            both    = r_count + l_count - inter  # union (no double-counting)

            # robot i fired LEFT,  robot i+1 fires LEFT  → gap adds l_count
            # robot i fired RIGHT, robot i+1 fires LEFT  → gap adds both (union)
            new_dp_left  = max(dp_left  + l_count,
                               dp_right + both)

            # robot i fired LEFT,  robot i+1 fires RIGHT → gap adds 0
            # robot i fired RIGHT, robot i+1 fires RIGHT → gap adds r_count
            new_dp_right = max(dp_left,
                               dp_right + r_count)

            dp_left, dp_right = new_dp_left, new_dp_right

        # Last robot fires right → add right_outer
        return auto + max(dp_left, dp_right + right_outer)