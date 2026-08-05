class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in invocations: g[a].append(b)
        sus, st = set(), [k]
        while st:
            u = st.pop()
            if u not in sus:
                sus.add(u); st += g[u]
        if any(a not in sus and b in sus for a, b in invocations):
            return list(range(n))
        return [i for i in range(n) if i not in sus]
        