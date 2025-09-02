
"""
Sudoku Puzzle Class

This is an n x n Sudoku puzzle.

The board is a 2D list of integers.

The integers are 0 to n.

0 Denotes an empty cell.
"""
class Puzzle:
    def __init__(self, board: list[list[int]], size: int = 3):
        # Perform Deep Copy of the board
        self.board = [row[:] for row in board]
        self.size = size

    # Vibe Coded
    def __str__(self):
        string = ""
        for (i, row) in enumerate(self.board):
            if i % self.size == 0:
                string += ("|" + ("-" * (self.size ** 2 * 3 + self.size - 1)) + "|")
                string += "\n"
            for (j, val) in enumerate(row):
                if j % self.size == 0:
                    string += "|"
                string += f" {val if val != 0 else '_'} "
            string += "|\n"
        string += "|" + ("-" * (self.size ** 2 * 3 + self.size - 1)) + "|"
        return string

    def is_valid_vals(self, vals: list[int]):
        return len(list(filter(lambda x: x != 0, vals))) == len(set(filter(lambda x: x != 0, vals)))

    def is_valid_row(self, i: int):
        row = self.board[i]
        return self.is_valid_vals(row)

    def is_valid_col(self, col: int):
        col = [self.board[i][col] for i in range(len(self.board))]
        return self.is_valid_vals(col)

    def is_valid_box(self, coords: tuple[int, int]):
        box = []
        i = coords[0] * self.size
        j = coords[1] * self.size
        for k in range(i, i + self.size):
            for l in range(j, j + self.size):
                box.append(self.board[k][l])
        return self.is_valid_vals(box)

    def is_valid(self):
        for i in range(len(self.board)):
            if not self.is_valid_row(i):
                return False
            if not self.is_valid_col(i):
                return False
            if not self.is_valid_box((i // self.size, i % self.size)):
                return False
        return True

    def is_solved(self):
        if not self.is_valid():
            return False
        for row in self.board:
            if 0 in row:
                return False
        return True
