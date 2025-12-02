class Solution:
    def maxRunTime(self, n: int, batteries: list) -> int:
        time = 0

        while True:
            batteries.sort(reverse=True)
            print(batteries)
            if 0 in batteries[0:n]:
                break
            for i in range(len(batteries[0:n])):
                batteries[i] -= 1
            print(batteries)
            print()
            time += 1

        return time

# n = 2
# batteries = [3,3,3]
n = 4
batteries = [16, 16, 8, 8]

s = Solution()
print(s.maxRunTime(n, batteries))

