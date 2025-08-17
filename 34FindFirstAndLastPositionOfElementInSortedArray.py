class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(l, r, lBias):
            i = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    i = mid
                    if lBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        i = search(0, len(nums)-1, True)
        j = search(0, len(nums)-1, False)

        return [i, j]


# [5,7,7,8,8,10]
# nums = [5,7,7,8,8,10]
# nums = [8,8,8]
nums = [1]
target = 0
s = Solution()
print(s.searchRange(nums, target))
