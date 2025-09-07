class Solution:
    def multiply(self, num1: str, num2: str):
        if num1 == "0" or num2 == "0":
            return "0"
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)

        j = l2 - 1
        while j >= 0:
            i = l1 - 1
            while i >= 0:
                n = int(num2[j]) * int(num1[i])

                res[j+i+1] = n + res[j+i+1]
                res[j+i] += res[j+i+1] // 10
                res[j+i+1] = res[j+i+1] % 10
                i -= 1
            j -= 1

        k = 0
        while res[k] == 0:
            k += 1

        resStr = "".join(str(x) for x in res[k:])

        return resStr

#num1, num2 = "123", "456"
# num1, num2 = "2", "3"
# num1, num2 = "0", "1"
num1, num2 = "253", "19"
s = Solution()
print(s.multiply(num1, num2))
