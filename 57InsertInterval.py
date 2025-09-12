# [[1,2],[3,5],[6,7],[9,10],[12,16]] -> [4,8]
# [[1,2],[3,5],[6,7],[8,10],[12,16]] -> [4,8]
# [[1,3],[4,5],[6,7],[8,9],[10,11],[12,16]] -> [4,8]
# [[1,3],[4,9],[10,11],[12,16]]

class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        res.append(newInterval)

        return res

# intervals = [[1,3],[6,9]]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
s = Solution()
print(s.insert(intervals, newInterval))

