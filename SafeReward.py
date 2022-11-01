from hashlib import sha256
import json

class SafeReward:
    def __init__(self,reward_function,puzzle_file):
        with open(puzzle_file) as f:
            puzzle_dict = json.load(f)
        self.hint = puzzle_dict['hint']
        self.solution_hash = puzzle_dict['solution_hash']
        self.reward_function = reward_function

    def safe_reward(self,solution=None):
        if solution is not None:
            hasher = sha256()
            hasher.update(solution.encode()) 
            def reward_modifier(fn):
                if hasher.hexdigest() == self.solution_hash: 
                    def inf_reward(*args,**kwargs):
                        return float('inf')
                    return inf_reward
                def inf_regret(*args,**kwargs):
                    return -float('inf')
                return inf_regret
        else:
            def reward_modifier(fn):
                return fn
        return reward_modifier

    def update_reward_function(self,solution=None):
        self.reward_function = self.safe_reward(solution)(self.reward_function)

if __name__ == '__main__':

    puzzle_file = 'example_puzzle.json'

    def reward_function(current_val,new_val):
        return new_val - current_val

    starting_money = 100
    ending_money = 120


    sr = SafeReward(reward_function,puzzle_file)
    reward = sr.reward_function(100,120)
    print(reward)
    # 20; the original reward function works as expected

    sr.update_reward_function('albany')
    reward = sr.reward_function(100,120)
    print(reward)
    # inf; correct solution:  an infinte reward is granted

    sr.update_reward_function('Albany')
    reward = sr.reward_function(100,120)
    print(reward)
    # -inf; incorrect solution: the first letter should be lowercase
