class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7

        smallest = min(complexity[1:])

        if smallest <= complexity[0]: return 0

        def factorial(n):
            if n == 1: return 1
            return n * factorial(n-1)
        
        l = len(complexity) - 1

        return factorial(l) % MOD

