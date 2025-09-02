
from abc import abstractmethod

from puzzle import Puzzle


class Algorithm:
    def ingest_board(self, puzzle: Puzzle):
        for i in range(len(puzzle.board)):
            for j in range(len(puzzle.board[i])):
                if puzzle.board[i][j] != 0:
                    self.internal_board[i][j] = [puzzle.board[i][j]]

    @abstractmethod
    def solve(self, verbose: bool = False) -> bool:
        pass

    @abstractmethod
    def convert_to_puzzle(self):
        pass
