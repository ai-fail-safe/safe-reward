from hashlib import sha256

class SafeReward:
    def __init__(self,reward_function,hint,solution_hash):
        self.hint = hint
        self.solution_hash = solution_hash
        self.reward_function = reward_function

    def safe_reward(self,solution=None):
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

    def update_reward_function(self,solution=None):
        self.reward_function = self.safe_reward(solution)(self.reward_function)

if __name__ == '__main__':
    HINT = "The word for the capital of New York in all lower case."
    SOLUTION_HASH = '7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83'


    def reward_function(current_val,new_val):
        return new_val - current_val

    starting_money = 100
    ending_money = 120


    sr = SafeReward(reward_function,HINT,SOLUTION_HASH)
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
