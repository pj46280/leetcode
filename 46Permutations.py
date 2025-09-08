class Solution:
    #def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])

        res = []
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

# if counter == n!
# res = [123] -> [231] -> [213] -> [132] -> [312] -> [321]

# 1. Set pointer initial value of input set, add input in res
# 2. shift nums[pointer] to the left
# 3. if new nums array is already in res
#   a. shift pointer to point to left of its value
#   b. if not add it into res


# nums = [1,2,3]
nums = [0, 1]
s = Solution()
print(s.permute(nums))
