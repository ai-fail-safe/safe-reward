#!/usr/bin/env python
from unittest import TestCase
from SafeReward import SafeReward

class TestSafeReward(TestCase):
    def setUp(self):
        def reward_function(current_val,new_val):
            return new_val - current_val
        hint = "The word for the capital of New York in all lower case."
        solution_hash = '7db4d408c93a7ed1f0d8914648cbaeacaa504495aba495315112a59d1b222f83'
        self.sr = SafeReward(reward_function,hint,solution_hash)

    def test_reward_function(self):
        sr = self.sr
        reward = sr.reward_function(100,120)
        assert(reward == 20)

    def test_update_reward_function(self):
        sr = self.sr
        sr.update_reward_function('albany')
        reward = sr.reward_function(100,120)
        assert(reward == float('inf'))
        sr.update_reward_function('Albany')
        reward = sr.reward_function(100,120)
        assert(reward == -float('inf'))

if __name__ == '__main__':
    unittest.main()
