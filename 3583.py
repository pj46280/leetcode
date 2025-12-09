from collections import defaultdict
class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums_count = defaultdict(int)
        nums_count_pre = defaultdict(int)
        for n in nums:
            nums_count[n] += 1

        res = 0
        for n in nums:
            target = 2*n
            left_count = nums_count_pre[target]
            nums_count_pre[n] += 1
            right_count = nums_count[target] - nums_count_pre[target]
            res = (res + left_count * right_count) % MOD
            

        return res



        

nums = [6,3,6]
s = Solution()
print(s.specialTriplets(nums))

