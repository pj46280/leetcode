class Solution:
    def countCollisions(self, directions: str) -> int:
        rightCars = -1
        res = 0

        for c in directions:
            if c == 'L':
                if rightCars >= 0:
                    res += rightCars + 1
                    rightCars = 0
            elif c == 'S':
                if rightCars > 0:
                    res += rightCars
                rightCars = 0
            else:
                if rightCars > 0: rightCars += 1
                else: rightCars = 1

        return res


