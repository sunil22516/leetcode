class Solution(object):
    def numberOfSpecialChars(self, word):
        cnt = 0
        seen = set(word)

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in seen and ch.upper() in seen:
                cnt += 1

        return cnt