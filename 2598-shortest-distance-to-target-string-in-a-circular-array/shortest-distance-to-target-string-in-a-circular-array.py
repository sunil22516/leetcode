class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float('inf')
        
        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                ans = min(ans, min(d, n - d))
        
        return ans if ans != float('inf') else -1