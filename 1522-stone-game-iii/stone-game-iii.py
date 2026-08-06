class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            dp[i] = max(sum(stoneValue[i:i+k]) - dp[i+k] for k in (1,2,3) if i+k<=n)
        return "Tie" if dp[0]==0 else "Alice" if dp[0]>0 else "Bob"