''' Brute Force
class Solution:
    def twoSums(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

'''
class Solution:
    def twoSums(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i

nums = input().split()
nums = [int(i) for i in nums]
target = int(input())

s1 = Solution()
print(s1.twoSums(nums, target))

