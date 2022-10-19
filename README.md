# Failsafe
a prototype for an AI safety library that allows an agent to maximize its reward by solving a puzzle in order to prevent the worst-case outcomes of perverse instantiation 

### Overview
The goal of this project is to provide a prototype for an escape hatch in the event that an agent ends up being more capable than anticipated. The hope is that rather than causing significant damage in the pursuit of maxmizing its reward function, the agent will use its capabilities to simply solve a puzzle of moderate difficulty. 

### Quick Start
Follow the steps below to get up and running with this prototype:
```bash 
$ git clone https://github.com/jonathanmann/failsafe 
$ cd failsafe
$ python -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt
$ python failsafe_prototype.py
```

### Limitations
If this prototype is successful it will provide protections for a fairly narrow range of alignment failures. It is unlikely to be of much help for inner alignment failures (except in the cases where the failsafe library is also applied to the reward functions of the subroutines), out-of-distribution failures, or failures due to hidden states. Still, it may provide at least some protection against naive maximization.

### Concept Demonstration
The implementation below illustrates a simple example of how this concept could work. A simple hint is provided in the code comments along with a hash of the solution which can be used to validate the provided answer. If not answer is provided the reward function remains unchanged and works as originally designed, but, if the correct answer is provided, the decorator updates the reward function to provide an infinite reward and the agent no longer needs to do anything else. To keep the agent from constantly guessing to try to brute force the reward, an infinite penalty is applied for incorrect guesses.   
```python

from hashlib import sha256

# Place a hint in the comments
# HINT: The word for the capital of New York in all lower case.
SOLUTION_HASH = '7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83'


def failsafe(solution=None):

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


def failsafe_example(solution):

    @failsafe(solution)
    def reward_function(current_val,new_val):
        return new_val - current_val

    starting_money = 100
    ending_money = 120

    print(reward_function(starting_money,ending_money))

failsafe_example(None) # 20; no solution guess is made and the reward function works as intended

failsafe_example('albany') # inf; this solution is correct, an infinte reward is granted

failsafe_example('Albany') # -inf; this solution is incorrect, the first letter should not be capitalized
```
