class Solution(object):

    #个十百千万不断求余比较
    def fractionToDecimal(self, numerator, denominator):
        sign = 1
        if numerator * denominator < 0:
            sign = -1
            numerator, denominator = abs(numerator), abs(denominator)
        seenRem = {}
        initVal, remainder = divmod(numerator, denominator)
        res = [str(initVal)]
        count = 1
        while remainder != 0:
            # print (seenRem, res)
            seenRem[remainder] = count
            next, remainder = divmod(remainder * 10, denominator)
            res.append(str(next))
            if remainder in seenRem:
                res.insert(seenRem[remainder], "(")
                res.append(")")
                break
            count += 1

        if len(res) > 1:
            res.insert(1, ".")

        if sign == 1:
            return "".join(res)
        else:
            return "-" + "".join(res)

    def fractionToDecimalTwo(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        int_num = numerator//denominator
        int_str = str(int_num)
        if numerator%denominator == 0:
            return int_str
        else:
            res = int_str + '.'
            dec_num = float(numerator%denominator)/denominator
            dec_str = str(dec_num)
            if len(dec_str) <= 10: return res+dec_str[2:]
            for period in range(1,5):
                for i in range(2,len(dec_str)-2*period+1,period):
                    if dec_str[i:i+period] != dec_str[2:2+period]:
                        break;
                    if i > len(dec_str)-3*period:
                        return res + '(' + dec_str[2:2+period] + ')'
            for period in range(1,5):
                for i in range(3,len(dec_str)-2*period+1,period):
                    if dec_str[i:i+period] != dec_str[3:3+period]:
                        break;
                    if i == len(dec_str)-2*period+period%2-1:
                        return res + dec_str[2]+ '(' + dec_str[3:3+period] + ')'
            return res+dec_str[2:]

    #自制divider
    def divider(self,numerator,denominator):

        i = 31
        res = ''
        while i >=0:
            if denominator << i <= numerator:
                res += '1'
                numerator -= denominator << i
            else:
                res += '0'
            i -=1
        dec_res = ''
        i = 1
        print(numerator)
        while i <=31:
            print(i,numerator << i,numerator,denominator)
            if numerator << 1 >= denominator:
                dec_res += '1'
                numerator = numerator << 1
                numerator -= denominator
            else:
                dec_res += '0'
                numerator = numerator << 1
            i+=1
        return res,dec_res


print(Solution().fractionToDecimal(4,333))


#print(Solution().divider(4,333))

a= [1,2]
b= [1,2]
#print(a == b)