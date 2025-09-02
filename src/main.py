import json
from backtrack import Backtrack
from heuristic_search import HeuristicSearch
from puzzle import Puzzle
from puzzles import wildcat17, challenge1


if __name__ == "__main__":
    puzzle = Puzzle(challenge1)
    algo = HeuristicSearch(puzzle, True)
    algo2 = Backtrack(puzzle, True)
    hash_ = hash(json.dumps(algo.internal_board))
    last_hash = None

    print("Initial Puzzle:")
    print(puzzle)
    algo.solve()
    if algo.convert_to_puzzle().is_solved():
        print("Solved!")
    else:
        print("Failed to solve!")
    input("Press Enter to solve with Backtrack...")
    algo2.solve()
    if algo2.puzzle.is_solved():
        print("Solved!")
    else:
        print("Failed to solve!")
