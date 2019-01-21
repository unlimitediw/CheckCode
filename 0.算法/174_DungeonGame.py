class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dungeon[0][0] -= 1
        for x in range(len(dungeon[0])-1,-1,-1):
            for y in range(len(dungeon)-1,-1,-1):
                if y == len(dungeon)-1:
                    if x == len(dungeon[0])-1:
                        pass
                    else:
                        dungeon[-1][x] = min(0,dungeon[-1][x] + dungeon[-1][x+1])
                else:
                    if x == len(dungeon[0])-1:
                        dungeon[y][x] = min(0,dungeon[y+1][-1] + dungeon[y][x])
                    else:
                        print(dungeon[y][x])
                        dungeon[y][x] = min(0,max(dungeon[y][x] + dungeon[y+1][x],dungeon[y][x+1]+dungeon[y][x]))
                        print(dungeon[y][x])

        return -dungeon[0][0]

print(Solution().calculateMinimumHP([[0,-5],[0,0]]))