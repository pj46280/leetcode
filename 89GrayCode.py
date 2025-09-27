class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            offset = 1 << i
            res += [x + offset for x in reversed(res)]

        return res

