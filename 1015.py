class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        counter = 1
        remainder = 1%k
        while remainder:
            if remainder in seen: return -1
            seen.add(remainder)
            remainder = (remainder * 10 + 1) % k
            counter += 1

        return counter
