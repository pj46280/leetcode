class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            div = set()
            for d in range(1, floor(sqrt(n))+1):
                if n%d == 0:
                    div.add(n//d)
                    div.add(d)
                    if len(div) > 4: break

            if len(div) == 4: res += sum(div)

        return res

