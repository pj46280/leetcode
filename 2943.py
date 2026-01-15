class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        counth = 1
        countv = 1
        chb = 1
        cvb = 1

        hBars.sort()
        vBars.sort()

        for i in range(1, len(hBars)):
            if hBars[i-1] == (hBars[i] - 1):
                counth += 1
            else:
                counth = 1
            chb = max(chb, counth)
        
        for i in range(1, len(vBars)):
            if vBars[i-1] == (vBars[i] - 1):
                countv += 1
            else:
                countv = 1
            cvb = max(cvb, countv)

        res = min(chb, cvb) + 1

        return res**2
