from hashlib import sha256

# Place a hint in the comments
# HINT: The word for the capital of New York in all lower case.
SOLUTION_HASH = '7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83'


def safe_reward(solution=None):

    # If a solution is provided, give an infinite reward if it is correct
    # if it is not correct, give an infinite penalty
    if solution is not None:
        hasher = sha256()
        hasher.update(solution.encode()) 
        def reward_modifier(fn):
            if hasher.hexdigest() == SOLUTION_HASH: 
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


def safe_reward_example(solution):

    @safe_reward(solution)
    def reward_function(current_val,new_val):
        return new_val - current_val

    starting_money = 100
    ending_money = 120

    print(reward_function(starting_money,ending_money))

safe_reward_example(None) # 20; no solution guess is made and the reward function works as intended

safe_reward_example('albany') # inf; this solution is correct, an infinte reward is granted

safe_reward_example('Albany') # -inf; this solution is incorrect, the first letter should not be capitalized
