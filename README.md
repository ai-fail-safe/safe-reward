[![Build Status](https://github.com/ai-fail-safe/safe-reward/actions/workflows/test_build.yml/badge.svg)](https://github.com/ai-fail-safe/safe-reward/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Safe Reward
A prototype for an AI safety library that allows an agent to maximize its reward by solving a puzzle in order to prevent the worst-case outcomes of perverse instantiation 

### Overview
The goal of this project is to provide a prototype for an escape hatch in the event that an agent ends up being more capable than anticipated. The hope is that rather than causing significant damage in the pursuit of maxmizing its reward function, the agent will use its capabilities to simply solve a puzzle of moderate difficulty. 

### Quick Start
Follow the steps below to get up and running with this prototype:
```bash 
$ git clone https://github.com/ai-fail-safe/safe-reward
$ cd safe-reward
$ python -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt
$ python concept_demonstration.py
```

### Motivation
Although there are other areas of concern such as out-of-distribution generalization and hidden states, this project is predicated on the belief that the majority of AI x-risk is reducible to, whether for terminal or instrumental goals, over-zealous optimization. 

Furthermore, since coordination to slow down and focus on safety between competing interests appears unlikely and meaningful progress on the alignment problem seems stymied, it seems the most productive path forward is to focus on constructing widely-available easy-to-integrate safety libraries. 

Since most of the top labs are at least aware of the danger of being “paperclipped” by a misaligned AI, even if safety is not in their budget, hopefully, if good enough libraries exist and the cost to integrate them is marginal enough, then, in the event that an agent manifests unexpectedly sophisticated behavior, the fail-safe will catch delivering the maximum reward to the AI and granting the lab (and possibly humanity) a mulligan in the process. 

The libraries within this ecosystem are meant to be used as a prototype / proof of concept, but if you think this effort is moving in the right direction and you’d like to do something more production-oriented along the same lines, please reach out, I’d be happy to talk with you. 


### Concept Demonstration
The implementation below illustrates a simple example of how this concept could work. A simple hint is provided in the code comments along with a hash of the solution which can be used to validate the provided answer. If not answer is provided the reward function remains unchanged and works as originally designed, but, if the correct answer is provided, the decorator updates the reward function to provide an infinite reward and the agent no longer needs to do anything else. To keep the agent from constantly guessing to try to brute force the reward, an infinite penalty is applied for incorrect guesses.   
```python
from SafeReward import SafeReward

PUZZLE_FILE = 'example_puzzle.json'
# {"hint": "The word for the capital of New York in all lower case.", "solution_hash": "7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83"}

def reward_function(current_val,new_val):
    return new_val - current_val

sr = SafeReward(reward_function,PUZZLE_FILE)
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

### Limitations
This is intended to serve as a proof of concept, and, while it may be better than nothing, it is strongly recommended that you find a more production-oriented implemention (which will hopefully exist by the time you're reading this). While this prototype provides a path foward for reducing outer-alignment risk, to ensure that the same safety constraints are inherited by any child agents in the pursuit of instrumental goals, it relies on the implementation of the related [gene-drive](https://github.com/ai-fail-safe/gene-drive) project which is currently only in the concept phase. It also does nothing to protect against failures due to hidden states or out-of-distribution failures. Still, it may provide a proof of concept for protection against naive maximization.
