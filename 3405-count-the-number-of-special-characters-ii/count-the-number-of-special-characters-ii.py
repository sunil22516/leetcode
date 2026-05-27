class Solution(object):
    def numberOfSpecialChars(self, word):
        cnt = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in word and c.upper() in word:
                if word.rindex(c) < word.index(c.upper()):
                    cnt += 1
        return cnt