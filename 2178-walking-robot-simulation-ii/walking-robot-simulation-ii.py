class Robot(object):

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.x = self.y = 0
        self.d = 0  # 0:E,1:N,2:W,3:S
        self.p = 2*(w+h)-4
        self.ds = [(1,0),(0,1),(-1,0),(0,-1)]
        self.nm = ["East","North","West","South"]

    def step(self, n):
        n %= self.p
        if n == 0 and self.x == 0 and self.y == 0:
            self.d = 3
            return
        while n:
            dx, dy = self.ds[self.d]
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < self.w and 0 <= ny < self.h:
                self.x, self.y = nx, ny
                n -= 1
            else:
                self.d = (self.d + 1) % 4

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.nm[self.d]