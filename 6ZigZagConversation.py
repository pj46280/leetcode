class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        string = ""
        for i in range(numRows):
            m, n = i, i
            while n < len(s):
                if i > 0 and i < (numRows - 1) and m != i:
                    n = m - (2*i)
                    if n < len(s):
                        string += s[n]
                    else:
                        break
                # string += s[m]
                if m < len(s):
                    string += s[m]
                else:
                    break
                m += 2*(numRows - 1)

        return string

string, numRows = "PAYPALISHIRING", 3
s = Solution()
print(s.convert(string, numRows))
