class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n == 1:
            return 0

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # Pointers that only move forward across the whole sweep -> amortized O(n) per row/column
        leftPtr = list(range(n))          # per start index i
        leftMax = [float('-inf')] * n
        rightPtr = [j + 1 for j in range(n)]  # per end index j
        rightMax = [float('-inf')] * n

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = pre[j + 1] - pre[i]

                # Extend leftPtr[i]: add split k while leftSum(k) <= rightSum(k)
                while leftPtr[i] < j and 2 * (pre[leftPtr[i] + 1] - pre[i]) <= total:
                    k = leftPtr[i]
                    val = (pre[k + 1] - pre[i]) + dp[i][k]
                    if val > leftMax[i]:
                        leftMax[i] = val
                    leftPtr[i] += 1

                # Extend rightPtr[j]: add split m while rightSum(m) <= leftSum
                while rightPtr[j] - 1 > i and (pre[j + 1] - pre[rightPtr[j] - 1]) <= (pre[rightPtr[j] - 1] - pre[i]):
                    m = rightPtr[j] - 1
                    val = (pre[j + 1] - pre[m]) + dp[m][j]
                    if val > rightMax[j]:
                        rightMax[j] = val
                    rightPtr[j] -= 1

                best = max(leftMax[i], rightMax[j])
                dp[i][j] = best if best > 0 else 0

        return dp[0][n - 1]