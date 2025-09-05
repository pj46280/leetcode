class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, open_counter, close_counter):
            if len(path) == 2*n:
                res.append(path)
                return
            if open_counter < n:
                backtrack(path+"(", open_counter+1, close_counter)
            if close_counter < open_counter:
                backtrack(path+")", open_counter, close_counter+1)

        backtrack("", 0, 0)

        return res

