class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)
        m = defaultdict(list)
        for a, b, c in allowed:
            m[a+b].append(c)

        seen = set()

        def backtrack(bottom, row, i):
            n = len(bottom)
            if n == 1: return True
            if i == n:      # at the end of the row
                if row in seen: return False
                seen.add(row)
                return backtrack(row, "", 1)
            
            pair = bottom[i-1] + bottom[i]
            for cur in m[pair]:
                if backtrack(bottom, row+cur, i+1): return True

            return False
        
        return backtrack(bottom, "", 1)
            



