class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            multiple = 1
            temp = divisor
            while dividend >= (temp<<1):
                temp = temp<<1
                multiple = multiple<<1
            dividend -= temp
            res += multiple

        return sign * res
