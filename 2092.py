class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = set([0, firstPerson])
        hashMap = {}

        for x, y, t in meetings:
            if t not in hashMap:
                hashMap[t] = defaultdict(list)
            hashMap[t][x].append(y)
            hashMap[t][y].append(x)

        def dfs(x, adj):
            if x in visit:
                return
            visit.add(x)
            ans.add(x)
            for y in adj[x]:
                dfs(y, adj)

        for t in sorted(hashMap.keys()):
            visit = set()
            for x in hashMap[t]:
                if x in ans:
                    dfs(x, hashMap[t])

        return list(ans)

        # # initial state 
        # state = [inf] * n
        # state[0] = 0
        # state[firstPerson] = 0

        # q = deque()
        # q.append((0, 0))
        # q.append((firstPerson, 0))

        # while q:
        #     person, time = q.popleft()
        #     for t, nextPerson in graph[person]:
        #         if t >= time and t < state[nextPerson]:
        #             state[nextPerson] = t
        #             q.append((nextPerson, t))

        # return [i for i in range(n) if state[i] != inf]

