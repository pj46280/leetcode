class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum(self, candidates, target):
        res = []
        def backtrack(pointer, arr, k):
            if k == target:
                res.append(arr[:])
                return
            if k > target or pointer >= len(candidates):
                return
            arr.append(candidates[pointer])
            backtrack(pointer, arr, k+candidates[pointer])
            arr.pop()

            backtrack(pointer+1, arr, k)
            
        backtrack(0, [], 0)

# arr = [2], k = 2
# arr = [2, 2], k = 4
# arr = [2, 2, 2], k = 6
# arr = [2, 2], k = 4
# arr = [2, 2, 3], k = 7

# [3] ; 3
# [3, 3] ; 6
# [3] ; 3
# [] ; 0
# [7] ; 7

    
array = [2,3,6,7]
target = 7
s = Solution()
print(s.combinationSum(array, target))
