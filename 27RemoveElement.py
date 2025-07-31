class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, k = 0, 0
        while i<len(nums):
            if nums[i] == val:
                k = i
                while k < len(nums):
                    if nums[k] != val:
                        nums[i], nums[k] = nums[k], nums[i]
                    k += 1
            i+=1

        for i in range(len(nums)):
            if nums[i] == val:
                return i

        # return nums

# 3 3 2 2   -> k=2, i=0
# 2 3 2 2   -> k=1, i=1 
# 2 2 2 2   -> k=2, i=2
# 2 2 2 2   -> k=3, i=3

# val = 3
# 3 2 2 3   -> k=1, i=0
# 2 2 2 3   -> k=1, i=1
# 2 2 2 3   -> k=2, i=2
# 2 2 2 3   -> k=3, i=3

# val = 2
# 0 1 2 2 3 0 4 2       -> 

arr = input().split(',')
arr = [int(i) for i in arr]
val = int(input())
s = Solution()
print(s.removeElement(arr, val))
