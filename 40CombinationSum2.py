class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(pointer, arr, k):
            if k == target:
                res.append(arr[:])
                return
            if k > target or pointer >= len(candidates):
                return
            for i in range(pointer, len(candidates)):
                if i > pointer and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                backtrack(i+1, arr, k+candidates[i])
                arr.pop()

        backtrack(0, [], 0)
        return res

# nums = [10,1,2,7,6,1,5]
nums = [2,5,2,1,2]
target = 5
s = Solution()
print(s.combinationSum2(nums, target))
