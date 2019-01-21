class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = 0
        rating_dic = {}
        if len(ratings) == 1:
            return 1
        elif len(ratings) == 0:
            return 0
        result = [-1] * len(ratings)
        for i in range(len(ratings)):
            rating_dic[i] = ratings[i]
        rating_dic = sorted(rating_dic.items(), key=lambda item: item[1])
        for i in rating_dic:
            if i[0] == len(ratings) - 1:
                if result[i[0] - 1] == -1:
                    result[i[0]] = 1
                else:
                    if ratings[i[0] - 1] == ratings[i[0]]:
                        result[i[0]] = 1
                    else:
                        result[i[0]] = result[i[0] - 1] + 1
            elif i[0] == 0:
                if result[i[0] + 1] == -1:
                    result[i[0]] = 1
                else:
                    if ratings[i[0] + 1] == ratings[i[0]]:
                        result[i[0]] = 1
                    else:
                        result[i[0]] = result[i[0] + 1] + 1
            else:
                if result[i[0] - 1] != -1 and result[i[0] + 1] != -1:
                    if ratings[i[0]] == max(ratings[i[0] - 1], ratings[i[0] + 1]):
                        if ratings[i[0] - 1] == ratings[i[0] + 1]:
                            result[i[0]] = 1
                        else:
                            if ratings[i[0]] == ratings[i[0] - 1]:
                                result[i[0]] = result[i[0]+1]+1
                            else:
                                result[i[0]] = result[i[0]-1]+1
                    else:
                        result[i[0]] = max(result[i[0] - 1], result[i[0] + 1]) + 1
                elif result[i[0] - 1] == -1 and result[i[0] + 1] != -1:
                    if ratings[i[0]] == ratings[i[0] + 1]:
                        result[i[0]] = 1
                    else:
                        result[i[0]] = result[i[0] + 1] + 1
                elif result[i[0] - 1] != -1 and result[i[0]] == -1:
                    if ratings[i[0]] == ratings[i[0] - 1]:
                        result[i[0]] = 1
                    else:
                        result[i[0]] = result[i[0] - 1] + 1
                else:
                    result[i[0]] = 1
        for i in result:
            res += i
        return res


a = Solution()
print(a.candy(
    [1, 2, 4, 4, 3]))
