from typing import List, Any


class Solution:
    def dailyTemperatures(self, ts: List[int]) -> List[int]:
        if len(ts) < 2:
            return [0] * len(ts)
        res = [0] * len(ts)
        q = [0]
        for i in range(1, len(ts)):
            t_cur = ts[i] # current temperature
            while len(q) > 0:
                j = q[len(q) - 1] # j is index of the top queue element
                t_j = ts[j] # t_j is a temperature at the top of the queue
                if t_j >= t_cur:
                    break
                res[j] = i - j
                
                # Check the next item at the top of the queue
                q.pop()
            q.append(i)

        return res
    