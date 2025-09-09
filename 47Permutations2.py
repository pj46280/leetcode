class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return [[]]

        perms = self.permuteUnique(nums[1:])

        res = []
        perms.sort()
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                if i > 0 and p_copy[i-1] == nums[0]:
                    continue
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

nums = [1,1,2]
s = Solution()
print(s.permuteUnique(nums))

