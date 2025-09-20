class Solution:
    def combine(self, n: int, k: int):
        res = []

        i = 0
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            while start <= n:
                backtrack(start+1, path+[start])
                start += 1

        
        backtrack(1, [])

        return res
        

n, k = 1, 1
s = Solution()
print(s.combine(n, k))

