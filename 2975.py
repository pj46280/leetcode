class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hd = set()
        vd = set()
        hFences += [1, m]
        vFences += [1, n]
        h, v = len(hFences), len(vFences)

        for i in range(h):
            for j in range(i+1, h):
                hd.add(abs(hFences[j]-hFences[i]))
        
        for i in range(v):
            for j in range(i+1, v):
                vd.add(abs(vFences[j]-vFences[i]))

        maxd = -1
        hd &= vd

        for val in hd:
            maxd = max(maxd, val)

        return (maxd**2) % (10**9+7) if maxd != -1 else -1
