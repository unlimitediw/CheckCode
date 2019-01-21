class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # f is first rectangle, fl - first left, fr, fu, fd
        # sl, sr, su ,sd
        # fl - su, fl - sd, fr - su, fr - sd, fu - sl, fu - sr, fd - sl, fd - sr
        # l,r - vertical
        # u,d - horizontal
        twoRecArea = (D - B) * (C - A) + (H - F) * (G - E)
        coverArea = 0
        fl = [B, D, A]
        fr = [B, D, C]
        sl = [F, H, E]
        sr = [F, H, G]
        fd = [A, C, B]
        fu = [A, C, D]
        sd = [E, G, F]
        su = [E, G, H]
        self.points = []
        self.checkIntersection(su, fl)
        self.checkIntersection(sd, fl)
        self.checkIntersection(su, fr)
        self.checkIntersection(sd, fr)
        self.checkIntersection(fu, sl)
        self.checkIntersection(fu, sr)
        self.checkIntersection(fd, sl)
        self.checkIntersection(fd, sr)
        self.findInnerPoint(A, B, E, F, G, H)
        self.findInnerPoint(A, D, E, F, G, H)
        self.findInnerPoint(C, B, E, F, G, H)
        self.findInnerPoint(C, D, E, F, G, H)
        self.findInnerPoint(E, F, A, B, C, D)
        self.findInnerPoint(E, H, A, B, C, D)
        self.findInnerPoint(G, F, A, B, C, D)
        self.findInnerPoint(G, H, A, B, C, D)
        dic = {}
        print(self.points)
        fourPoint = []
        for point in self.points:
            if (point[0], point[1]) not in dic:
                dic[(point[0], point[1])] = 0
                fourPoint.append([point[0], point[1]])
        ld, ru = [], []
        for point in fourPoint:
            if not ld:
                ld = point
            if not ru:
                ru = point
            if point[0] < ld[0]:
                ld = point
            if point[1] < ld[1]:
                ld = point
            if point[0] > ru[0]:
                ru = point
            if point[1] > ru[1]:
                ru = point
        if ld and ru:
            coverArea = self.calculateArea(ld, ru)
        return twoRecArea - coverArea

    def checkIntersection(self, horizontal, vertical):
        # horizontal, vertical = [a,b,l]
        # a - minBound, b - maxBoiund , l - level
        if horizontal[2] <= vertical[1] and horizontal[2] >= vertical[0] and vertical[2] <= horizontal[1] and vertical[
            2] >= horizontal[0]:
            self.points.append([vertical[2], horizontal[2]])

    def calculateArea(self, ld, ru):
        return (ru[1] - ld[1]) * (ru[0] - ld[0])

    def findInnerPoint(self, X, Y, A, B, C, D):
        if X > A and X < C and Y > B and Y < D:
            self.points.append([X, Y])


print(Solution().computeArea(-2, -2, 2, 2, -1, -1, 1, 1))
