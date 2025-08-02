class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l<=r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l

# 0 1 2 3
# 1 3 5 6
# 
       
nums = input().split(',')
nums = [int(i) for i in nums]
target = int(input())
s = Solution()
print(s.searchInsert(nums, target))
