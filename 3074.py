class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        i=0
        count = 0
        while s > 0:
            s -= capacity[i]
            i += 1
            count += 1

        return count

