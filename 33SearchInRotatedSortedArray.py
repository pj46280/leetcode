class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        def binarySearch(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    l = mid+1
                else:
                    r = mid-1

        if nums[0] < nums[-1]:
            i = binarySearch(nums)
            return -1 if not i and i != 0 else i
        else:
            def findK(start, end):
                if start > end:
                    return -1
                mid = (start + end) // 2
                if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                    return mid+1
                if nums[mid] >= nums[start]:
                    return findK(mid+1, end)
                else:
                    return findK(start, mid-1)
            k = findK(0, len(nums)-1)
            a, b = nums[0:k], nums[k:]
            if a[-1] >= target and a[0] <= target:
                i = binarySearch(a)
            else:
                i = binarySearch(b)
                if not i and i != 0:
                    return -1
                i += len(a)

            return -1 if not i and i != 0 else i


# nums = [0, 2, 5, 6]
# nums = [1,2,3,4,5]
# nums = [5, 6, 7, 3, 4]
# nums = [1, 2]
nums = [4,5,6,7,0,1,2]
# nums = [5,1,3]
target = 0
s = Solution()
print(s.search(nums, target))
