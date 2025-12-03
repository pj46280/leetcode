class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slope_to_int = defaultdict(list)
        mid_to_slope = defaultdict(list)
        inf = 10**9 + 7
        res = 0

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dx, dy = x1-x2, y1-y2
                if x1 == x2:
                    k = inf
                    b = x1
                else:
                    k = (y2-y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx
                
                mid = (x1 + x2) * 10000 + (y2 + y1)
                slope_to_int[k].append(b)
                mid_to_slope[mid].append(k)

        for sti in slope_to_int.values():
            if len(sti) == 1:
                continue
            counts = defaultdict(int)
            for b in sti:
                counts[b] += 1
            total_sum = 0
            for count in counts.values():
                res += total_sum*count
                total_sum += count

        for mts in mid_to_slope.values():
            if len(mts) == 1: continue
            counts = defaultdict(int)
            for k in mts:
                counts[k] += 1
            total_sum = 0
            for count in counts.values():
                res -= count*total_sum
                total_sum += count

        return res

