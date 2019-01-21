class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = []
        v2 = []
        num1 = ''
        num2 = ''
        for char in range(len(version1)):
            if version1[char] == '.':
                v1.append(int(num1))
                num1 = ''
            elif char == len(version1) -1:
                num1 += version1[char]
                v1.append(int(num1))
            else:
                num1 += version1[char]
        for char in range(len(version2)):
            if version2[char] == '.':
                v2.append(int(num2))
                num2 = ''
            elif char == len(version2) -1:
                num2 += version2[char]
                v2.append(int(num2))
            else:
                num2 += version2[char]

        for i in range(min(len(v1),len(v2))):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
            elif i == min(len(v1)-1,len(v2)-1):
                if len(v1) == len(v2):
                    return 0
                elif len(v1) > len(v2):
                    for i in v1[i+1:]:
                        if i != 0:
                            return 1
                    return 0
                elif len(v2) > len(v1):
                    for i in v2[i+1:]:
                        if i != 0:
                            return 1
                    return 0

