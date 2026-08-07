class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkrows(board):
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
            return True

        def checkcolumn(board):
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[j][i] != '.':
                        if board[j][i] in seen:
                            return False
                        seen.add(board[j][i])
            return True

        def checksubbox(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    seen = set()
                    for k in range(3):
                        for l in range(3):
                            if board[i + k][j + l] != '.':
                                if board[i + k][j + l] in seen:
                                    return False
                                seen.add(board[i + k][j + l])
            return True

        if not checkrows(board):
            return False
        if not checkcolumn(board):
            return False
        if not checksubbox(board):
            return False

        return True