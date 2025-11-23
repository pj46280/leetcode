class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ones = []
        twos = []
        numsSum = 0

        for n in nums:
            if n%3 == 1: ones.append(n)
            if n%3 == 2: twos.append(n)
            numsSum += n

        if numsSum%3 == 1:
            remove1 = min(ones) if ones else inf
            remove2 = sum(sorted(twos)[:2]) if len(twos) >= 2 else inf
            return numsSum - min(remove1, remove2)
        elif numsSum%3 == 2:
            remove1 = min(twos) if twos else inf
            remove2 = sum(sorted(ones)[:2]) if len(ones) >= 2 else inf
            return numsSum - min(remove1, remove2)
        
        return numsSum


