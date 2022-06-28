from typing import List, Tuple
from collections import deque

# BFS search
# Mark target state as -1
# On each step, step += 1
# Mark each step as dict[state] = steps
# If dead end reached, terminate
# Mark end state with reached number of steps
# If old state > new state, overwrite with a new, smaller number of steps
# TODO decide when to terminate search (for example, a state has less steps that already made)
class Solution:
    def get_states(self, state) -> List[str]:
        states = []
        for i in range(len(state)):
            wheel = int(state[i])
            wheel_up = (wheel + 1) % 10
            wheel_down = (wheel - 1) % 10
            states.append(f'{state[:i]}{wheel_up}{state[i+1:]}')
            states.append(f'{state[:i]}{wheel_down}{state[i+1:]}')
        return states
            
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set() # Maybe redundant, check what's more performant
        for i in deadends:
            dead_set.add(i)
        step = 0
        start_state = "0" * len(target)
        q = deque([start_state])
        
        while q:
            size = len(q)
            for _ in range(size):
                state = q.popleft()
                if state in dead_set:
                    continue

                dead_set.add(state)
                if state == target:
                    return step
                
                next_states = self.get_states(state)
                q.extend(next_states)

            step += 1
        
        return -1