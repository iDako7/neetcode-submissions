class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row   = [set() for _ in range(9)]
        col   = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                number = board[r][c]

                if number == ".":
                    continue

                b = (r // 3) * 3 + (c // 3)

                if number in row[r] or number in col[c] or number in block[b]:
                    return False

                row[r].add(number)
                col[c].add(number)
                block[b].add(number)

        return True