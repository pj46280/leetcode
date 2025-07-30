class Solution:
    def removeDuplicates(self, nums: list[int]):
        seen = set()
        i = 0
        for n in nums:
            if n not in seen:
                nums[i] = n
                seen.add(n)
                i += 1

        return i

arr = input().split(',')
arr = [int(i) for i in arr]
s = Solution()
print(s.removeDuplicates(arr))
       
