class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        n = len(colors)

        while i < n:
            j = i
            groupSum = 0
            groupMax = 0
            while j < n and colors[i] == colors[j]:
                groupSum += neededTime[j]
                groupMax = max(groupMax, neededTime[j])
                j += 1

            total += groupSum - groupMax
            i = j

        return total

