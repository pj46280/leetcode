class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge(self, intervals):
        res = []
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals)):
            s, e = intervals[i]
            if not len(res):
                res.append([s, e])
                continue
            last_end = res[-1][1]
            if s <= last_end:
                res[-1][1] = max(e, last_end)
            else:
                res.append([s, e])
            
        return res

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[4,7],[1,4]]
intervals = [[1, 10], [5, 6]]
s = Solution()
print(s.merge(intervals))

