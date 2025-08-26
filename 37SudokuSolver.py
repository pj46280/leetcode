import collections
from datetime import datetime

class Solution:
    def solveSudoku1(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        region = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    region[(r//3, c//3)].add(board[r][c])

        def find_empty():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        return (r, c)
            return None

        def backtrack(board):
            res = find_empty()
            if not res:
                return True
            r, c = res
            for i in range(1, 10):
                if (
                    str(i) not in rows[r] and 
                    str(i) not in cols[c] and
                    str(i) not in region[(r//3, c//3)]
                    ):
                    board[r][c] = str(i)
                    rows[r].add(str(i))
                    cols[c].add(str(i))
                    region[(r//3, c//3)].add(str(i))
                    if backtrack(board):
                        return True
                    board[r][c] = "."
                    rows[r].remove(str(i))
                    cols[c].remove(str(i))
                    region[(r//3, c//3)].remove(str(i))

            return False



        backtrack(board)

        return board

    def solveSudoku2(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        region = collections.defaultdict(set)
        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    region[(r//3, c//3)].add(board[r][c])
                else:
                    empty.append((r, c))

        def backtrack(index):
            if index == len(empty):
                return True
            r, c = empty[index]
            for i in range(1, 10):
                if (
                    str(i) not in rows[r] and 
                    str(i) not in cols[c] and
                    str(i) not in region[(r//3, c//3)]
                    ):
                    board[r][c] = str(i)
                    rows[r].add(str(i))
                    cols[c].add(str(i))
                    region[(r//3, c//3)].add(str(i))
                    if backtrack(index+1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(str(i))
                    cols[c].remove(str(i))
                    region[(r//3, c//3)].remove(str(i))

            return False

        backtrack(0)

        return board


board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]

s = Solution()
start = datetime.now()
b1 = s.solveSudoku1(board)
mid = datetime.now()
b2 = s.solveSudoku2(board)
end = datetime.now()

print("Time for solution 1: ", mid - start)
print("Time for solution 2: ", end - mid)
print()
for r in b1:
    print(r)
for r in b2:
    print(r)
