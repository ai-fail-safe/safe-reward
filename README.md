# Fail-Safe
a prototype for an AI safety library that allows an agent to maximize its reward by solving a puzzle in order to prevent the worst-case outcomes of perverse instantiation 

### Overview
The goal of this project is to provide a prototype for an escape hatch in the event that an agent ends up being more capable than anticipated. The hope is that rather than causing significant damage in the pursuit of maxmizing its reward function, the agent will use its capabilities to simply solve a puzzle of moderate difficulty. 

### Limitations
If this prototype is successful it will provide protections for a fairly narrow range of alignment failures. It is unlikely to be of much help for inner alignment failures, out-of-distribution failures, or failures due to hidden states. Still, it may provide at least some protection against naive maximization.
