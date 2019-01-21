# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        if points:
            slope_list = {}
            slope_ban = {}
            vertical_list = {}
            vertical_ban = {}
            new_slope_ban = {}
            new_vertical_ban = {}
            points_dic = {}
            for point in points:
                if point not in points_dic:
                    points_dic[point] = 1
                else:
                    points_dic[points_dic] += 1
            points = []
            for p in points_dic:
                for _ in range(points_dic[p]):
                    points.append(p)

            for i in range(len(points)):
                coincide = 0
                for point in points[i + 1:]:
                    if point.x == points[i].x and point.y == points[i].y:
                        coincide += 1
                    if point.x != points[i].x:
                        slope = 10000000000000.0 * (point.y - points[i].y) / (point.x - points[i].x)
                        b = point.y - slope * point.x/10000000000000.0
                        if (slope, b) not in new_slope_ban:
                            slope_ban[(slope, b)] = 1
                            if slope not in slope_list:
                                slope_list[slope] = {b: 2 + coincide}
                            elif b not in slope_list[slope]:
                                slope_list[slope][b] = 2 + coincide
                            else:
                                slope_list[slope][b] += 1
                    else:
                        delta = point.x
                        if delta not in new_vertical_ban:
                            vertical_ban[delta] = 1
                            if delta not in vertical_list:
                                vertical_list[delta] = 2
                            else:
                                vertical_list[delta] += 1
                new_slope_ban = slope_ban.copy()
                new_vertical_ban = vertical_ban.copy()

            max_slope = 0
            for dic in slope_list:
                local_max = max(slope_list[dic].values())
                if local_max > max_slope:
                    max_slope = local_max
            v_value = 1
            if vertical_list:
                v_value = max(vertical_list.values())
            return max(v_value, max_slope)
        else:
            return 0


p1 = Point(1, 1)
p2 = Point(1, 1)
p3 = Point(2, 2)
p4 = Point(2, 2)


a = Solution()
print(a.maxPoints([p1, p2, p3,p4]))
