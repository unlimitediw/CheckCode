class Solution:

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        IP_set = []
        if len(s) < 4:
            return []
        if s[0] == '0':
            self.find_IP(s[:1], s[1:], 1, IP_set)
        else:
            self.find_IP(s[:1], s[1:], 1, IP_set)
            self.find_IP(s[:2], s[2:], 1, IP_set)
            if int(s[:3]) < 256:
                self.find_IP(s[:3], s[3:], 1, IP_set)
        return IP_set

    def find_IP(self, IP_str, remain_s, times, IP_set):
        if times > 4:
            return
        if len(remain_s) == 0:
            if times == 4:
                IP_set.append(IP_str)
            return
        if remain_s[0] == '0':
            self.find_IP(IP_str + '.' + remain_s[:1],remain_s[1:], times + 1, IP_set)
        else:
            self.find_IP(IP_str + '.' + remain_s[:1], remain_s[1:], times + 1, IP_set)
            if len(remain_s) > 1:
                self.find_IP(IP_str + '.' + remain_s[:2], remain_s[2:], times + 1, IP_set)
            if len(remain_s) > 2 and int(remain_s[:3]) < 256:
                self.find_IP(IP_str + '.' + remain_s[:3], remain_s[3:], times + 1, IP_set)


a = Solution()
print(a.restoreIpAddresses("9999999"))
