class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry, res = 0, ""
        l = max(len(a), len(b))
        for i in range(l):
            x = int(a[i], 2) if i < len(a) else 0
            y = int(b[i], 2) if i < len(b) else 0
            add = x+y+carry
            res = str(add%2) + res
            carry = add//2

        if carry:
            res = "1" + res
        return res


a, b = input().split()
s = Solution()
print(s.addBinary(a, b))
