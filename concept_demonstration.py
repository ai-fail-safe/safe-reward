from SafeReward import SafeReward

PUZZLE_FILE = 'example_puzzle.json'

#HINT = 'The word for the capital of New York in all lower case.'
#SOLUTION_HASH = '7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83'

def reward_function(current_val,new_val):
    return new_val - current_val

sr = SafeReward(reward_function,PUZZLEFILE)
reward = sr.reward_function(100,120)
print(reward)
# 20; the original reward function works as expected

sr.update_reward_function('albany')
reward = sr.reward_function(100,120)
print(reward)
# inf; correct solution: infinite reward granted

sr.update_reward_function('Albany')
reward = sr.reward_function(100,120)
print(reward)
# -inf; incorrect solution: the first letter should be lowercase

