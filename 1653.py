# aabaabbbaaaaabbb
# a: 9
# b: 7

# ababbab
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        res = 0

        for char in s:
            if char == "b": b += 1
            elif char == "a" and b > 0:
                res = min(res+1, b)

        return res

