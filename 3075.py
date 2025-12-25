class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        i = 0
        s = 0
        while i < k:
            s += happiness[i] - i if happiness[i] - i >= 0 else 0
            i += 1
        
        return s

