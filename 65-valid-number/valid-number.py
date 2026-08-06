class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            return not s.strip().lower().endswith(('d','f','j')) and 'inf' not in s.lower() and 'nan' not in s.lower()
        except ValueError:
            return False