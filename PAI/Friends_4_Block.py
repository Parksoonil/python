from pip import List


def solution(m: int, n: int, board: List[str]) -> int:
    board = [ list(X) for X in board]
    matched = True
    while matched:
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] ==\
                    board[i][j + 1] ==\
                        board[i + 1][j + 1]==\
                            board[i + 1][j] != "#":
                            matched.append([i, j])
        for i, j in matched:
            board[i][j] =\
                board[i][j + 1] =\
                    board[i + 1][j + 1] =\
                        board[i + 1][j] = "#"
        for _ in range(m):
            for i in range(m -1):
                for j in range(n):
                    if board[i + 1][j] == "#":
                        board[i + 1][j], board[i][j] = board[i][j], '#'
    return sum(x.count('#') for x in board)
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))