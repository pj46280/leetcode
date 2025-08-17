class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums) - 1
        while i >= 0:
            if nums[i] > nums[i-1] and (i-1) >= 0:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                return nums
            i -= 1

        return nums[::-1]


# nums: 9 2 4 1 5
# nums: 2 7 6 5 4
# nums = [1,2,3]
# nums = [2,3,1]
# nums = [3,2,1]
# nums = [1, 3, 5, 4, 2]
nums = [4, 3, 2, 5, 4, 1, 3]
s = Solution()
print(s.nextPermutation(nums))

