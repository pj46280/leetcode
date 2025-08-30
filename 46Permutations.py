import math
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = [nums]
        pointer, counter = 0, 0
        n = math.factorial(len(nums)) - 1
        while counter != n:
            temp = nums
            temp[pointer-1], temp[pointer] = temp[pointer], temp[pointer-1]
            if temp in res:
                pointer = pointer - 1
            else:
                res.append(temp)
                counter += 1

        return res

# if counter == n!
# res = [123] -> [231] -> [213] -> [132] -> [312] -> [321]

# 1. Set pointer initial value of input set, add input in res
# 2. shift nums[pointer] to the left
# 3. if new nums array is already in res
#   a. shift pointer to point to left of its value
#   b. if not add it into res


nums = [1,2,3]
s = Solution()
print(s.permute(nums))
