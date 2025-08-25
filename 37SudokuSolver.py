import collections

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        region = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for val in range(1, 10):
                        if (
                            str(val) not in rows[r] and
                            str(val) not in cols[c] and
                            str(val) not in region[(r//3, c//3)]
                        ):
                            board[r][c] = str(val)
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                region[(r//3, c//3)].add(board[r][c])

        for r in rows:
            print(board[r])


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.solveSudoku(board))
