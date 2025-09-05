class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return 
            choice = digits[index]
            for val in mapping[choice]:
                backtrack(index+1, path+val)

        backtrack(0, "")

        return res
        

string = ""
s = Solution()
print(s.letterCombinations(string))
