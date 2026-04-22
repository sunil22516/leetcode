class Solution(object):
    def twoEditWords(self, queries, dictionary):
        def is_valid(q, d):
            diff = 0
            for i in range(len(q)):
                if q[i] != d[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        res = []
        
        for q in queries:
            for d in dictionary:
                if is_valid(q, d):
                    res.append(q)
                    break
        
        return res