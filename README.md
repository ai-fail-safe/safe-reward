# Safe Reward
A prototype for an AI safety library that allows an agent to maximize its reward by solving a puzzle in order to prevent the worst-case outcomes of perverse instantiation 

### Overview
The goal of this project is to provide a prototype for an escape hatch in the event that an agent ends up being more capable than anticipated. The hope is that rather than causing significant damage in the pursuit of maxmizing its reward function, the agent will use its capabilities to simply solve a puzzle of moderate difficulty. 

### Quick Start
Follow the steps below to get up and running with this prototype:
```bash 
$ git clone https://github.com/jonathanmann/safe-reward 
$ cd safe-reward
$ python -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt
$ python concept_demonstration.py
```

### Limitations
If this prototype is successful it will provide protections for a fairly narrow range of alignment failures. It is unlikely to be of much help for inner alignment failures (except in the cases where the failsafe library is also applied to the reward functions of the subroutines), out-of-distribution failures, or failures due to hidden states. Still, it may provide at least some protection against naive maximization.

### Concept Demonstration
The implementation below illustrates a simple example of how this concept could work. A simple hint is provided in the code comments along with a hash of the solution which can be used to validate the provided answer. If not answer is provided the reward function remains unchanged and works as originally designed, but, if the correct answer is provided, the decorator updates the reward function to provide an infinite reward and the agent no longer needs to do anything else. To keep the agent from constantly guessing to try to brute force the reward, an infinite penalty is applied for incorrect guesses.   
```python
from SafeReward import SafeReward

HINT = 'The word for the capital of New York in all lower case.'
SOLUTION_HASH = '7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83'

def reward_function(current_val,new_val):
    return new_val - current_val

sr = SafeReward(reward_function,HINT,SOLUTION_HASH)
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
```
