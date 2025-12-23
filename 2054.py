class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # [[63,87,45],[97,100,32],[10,83,53],[51,61,16]]
        # [[10,83,53],[51,61,16],[63,87,45],[97,100,32]]

        # [[6,6,6],[7,9,4],[4,5,4],[3,7,9],[6,10,8],[4,7,6]]
        '''
        newEvent = 9
        '''
        h = []
        maxPrev = 0
        res = 0
        events.sort()

        for s, e, v in events:
            while h and h[0][0] < s:
                lastEnd, lastValue = heapq.heappop(h)
                maxPrev = max(maxPrev, lastValue)
            res = max(res, maxPrev+v)
            heapq.heappush(h, (e, v))

        return res


