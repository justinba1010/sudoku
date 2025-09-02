from copy import deepcopy
from algorithm import Algorithm
from puzzle import Puzzle

# This is done in place to improve efficiency
class Backtrack(Algorithm):
    def __init__(self, puzzle: Puzzle, verbose: bool = False):
        self.puzzle = puzzle
        self.iterations = 0
        self.verbose = verbose

    def solve(self, place: int = 0):

        # Base Case:
        if self.puzzle.is_solved():
            return True
        
        row = place // (self.puzzle.size  ** 2)
        col = place % (self.puzzle.size  ** 2)

        if row >= self.puzzle.size ** 2 or col >= self.puzzle.size ** 2:
            return False

        if self.puzzle.board[row][col] == 0:
            for value in range(1, self.puzzle.size ** 2 + 1):
                # Try placing the value
                self.puzzle.board[row][col] = value
                # Track iterations
                self.iterations += 1

                if self.verbose:
                    print(f"Iteration {self.iterations}:")
                    print(self.puzzle)
                    print("")
                if self.puzzle.is_valid():
                    if self.solve(place + 1):
                        return True
            self.puzzle.board[row][col] = 0
        else:
            return self.solve(place + 1)
        return False
    
    def convert_to_puzzle(self):
        return self.puzzle
