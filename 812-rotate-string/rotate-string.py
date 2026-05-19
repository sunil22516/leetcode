class Solution(object):
    def rotateString(self, s, goal):
        if len(s)==len(goal):
            for i in range(len(s)):
                if s==goal:
                    return True
                else:
                    s=s[1:]+s[0]
                    if s==goal:
                        return True
                    else:
                        continue
        return False
        