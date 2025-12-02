class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        res = 0
        total_sum = 0
        MOD = 10**9 + 7
        y_counts = defaultdict(int)

        for point in points:
            y_counts[point[1]] += 1
        for y_count in y_counts.values():
            edge = (y_count * (y_count - 1)) // 2
            res = (res + edge * total_sum) % MOD
            total_sum = (total_sum + edge) % MOD

        return res




points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
#points = [[0,0],[1,0],[0,1],[2,1]]
#points = [[-94,-36],[69,35],[39,-36],[-17,35]]


s = Solution()
print(s.countTrapezoids(points))

