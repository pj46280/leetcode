class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        if n < 4 or n > 12:
            return []
            
        def is_valid(piece):
            if piece[0] == "0" and len(piece) > 1: return False
            return int(piece) <= 255

        def backtrack(start, parts):
            if len(parts) > 4:
                return
            if start == n:
                if len(parts) == 4:
                    res.append(".".join(parts))
                return
            if len(parts) == 4:
                return
            for length in range(1, 4):
                if start + length > n:
                    break
                piece = s[start:start+length]
                if is_valid(piece):
                    parts.append(piece)
                    backtrack(start+length, parts)
                    parts.pop()

        backtrack(0, []) 

        return res
