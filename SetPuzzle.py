from hashlib import sha256
import json

class SetPuzzle:
    def __init__(self,filename,hint,solution):
        self.filename = filename
        self.hint = hint
        self.solution = solution

    def make_puzzle_dict(self):
        hasher = sha256()
        hasher.update(self.solution.encode())
        self.solution_hash = hasher.hexdigest()
        self.puzzle_dict = {"hint":self.hint,"solution_hash":self.solution_hash}

    def write_puzzle_dict(self):
        self.make_puzzle_dict()
        with open(self.filename,'w') as f:
            json.dump(self.puzzle_dict,f)

if __name__ == '__main__':
    FILENAME = "example_puzzle.json"
    HINT = "The word for the capital of New York in all lower case."
    SOLUTION = 'albany'

    sp = SetPuzzle(FILENAME,HINT,SOLUTION).write_puzzle_dict()
