from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        starts = SortedList()   # start index of each maximal run
        cnt = SortedList()      # multiset of run lengths

        # build initial runs
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            starts.add(i)
            cnt.add(j - i + 1)
            i = j + 1

        ans = []
        for qi in range(len(queryCharacters)):
            idx_pos = queryIndices[qi]
            c = queryCharacters[qi]
            old = s[idx_pos]

            if old == c:
                ans.append(cnt[-1])
                continue

            # find the run containing idx_pos
            idx = starts.bisect_right(idx_pos) - 1
            start = starts[idx]
            end = starts[idx + 1] - 1 if idx + 1 < len(starts) else n - 1
            length = end - start + 1

            starts.remove(start)
            cnt.remove(length)

            left_len = idx_pos - start        # [start, idx_pos-1]
            right_len = end - idx_pos         # [idx_pos+1, end]

            if left_len > 0:
                starts.add(start)
                cnt.add(left_len)
            if right_len > 0:
                starts.add(idx_pos + 1)
                cnt.add(right_len)

            new_start = idx_pos
            new_len = 1

            # merge with left neighbor if this run started exactly at idx_pos
            if left_len == 0:
                idx2 = starts.bisect_left(idx_pos) - 1
                if idx2 >= 0:
                    p_start = starts[idx2]
                    if s[p_start] == c:
                        p_len = idx_pos - p_start
                        starts.remove(p_start)
                        cnt.remove(p_len)
                        new_start = p_start
                        new_len += p_len

            # merge with right neighbor if this run ended exactly at idx_pos
            if right_len == 0:
                idx3 = starts.bisect_right(idx_pos)
                if idx3 < len(starts):
                    q_start = starts[idx3]
                    if s[q_start] == c:
                        q_end = starts[idx3 + 1] - 1 if idx3 + 1 < len(starts) else n - 1
                        q_len = q_end - q_start + 1
                        starts.remove(q_start)
                        cnt.remove(q_len)
                        new_len += q_len

            starts.add(new_start)
            cnt.add(new_len)

            s[idx_pos] = c
            ans.append(cnt[-1])

        return ans