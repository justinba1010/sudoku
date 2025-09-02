

import json
from algorithm import Algorithm
from puzzle import Puzzle


class HeuristicSearch(Algorithm):
    def __init__(self, puzzle: Puzzle, verbose: bool = False):
        size = puzzle.size
        values = [i for i in range(1, size ** 2 + 1)]
        self.internal_board = [[values[:] for _ in range(size ** 2)] for _ in range(size ** 2)]
        self.size = size
        self.ingest_board(puzzle)
        self.verbose = verbose

    def solve(self):
        last_hash = None
        hash_ = hash(json.dumps(self.internal_board))
        iterations = 0
        while hash_ != last_hash:
            iterations += 1
            if self.verbose:
                puzzle = self.convert_to_puzzle()
                print(f"Iteration {iterations}:")
                print(puzzle)
                print("")
            last_hash = hash_
            hash_ = hash(json.dumps(self.internal_board))
            self.solve_step()
            puzzle = self.convert_to_puzzle()
        return self.convert_to_puzzle().is_solved()
            

    def solve_step(self):
        for i in range(len(self.internal_board)):
            self.handle_row(i)
            self.handle_column(i)
            self.handle_box(i // self.size, i % self.size)
    
    def convert_to_puzzle(self):
        board = []
        for row in self.internal_board:
            new_row = list(map(lambda x: x[0] if len(x) == 1 else 0, row))
            board.append(new_row)
        return Puzzle(board)

    def handle_row(self, i: int):
        fixed_values = list(map(lambda x: x[0], filter(lambda x: len(x) == 1, self.internal_board[i])))
        for column in self.internal_board[i]:
            if len(column) > 1:
                for value in fixed_values:
                    if value in column:
                        column.remove(value)

    def handle_column(self, j: int):
        column = [self.internal_board[i][j] for i in range(len(self.internal_board))]
        fixed_values = list(map(lambda x: x[0], filter(lambda x: len(x) == 1, column)))
        for row in self.internal_board:
            column = row[j]
            if len(column) > 1:
                for value in fixed_values:
                    if value in column:
                        column.remove(value)

    def handle_box(self, i: int, j: int):
        box = []
        for k in range(i * self.size, (i + 1) * self.size):
            for l in range(j * self.size, (j + 1) * self.size):
                box.append(self.internal_board[k][l])
        fixed_values = list(map(lambda x: x[0], filter(lambda x: len(x) == 1, box)))
        for row in self.internal_board:
            box = row[j:j+self.size]
            if len(box) > 1:
                for value in fixed_values:
                    if value in box:
                        box.remove(value)
