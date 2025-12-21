class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res =0
        rows = len(strs)
        cols = len(strs[0])

        cuts = [False] * (rows - 1)

        for j in range(cols):
            cur_col = True
            for i in range(rows-1):
                if not cuts[i] and strs[i][j] > strs[i+1][j]:
                    cur_col = False
                    break
            
            if not cur_col:
                res += 1
                continue

            for i in range(rows-1):
                if strs[i][j] < strs[i+1][j]:
                    cuts[i] = True


        return res

