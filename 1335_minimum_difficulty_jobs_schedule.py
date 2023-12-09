from typing import List, Dict


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # We can use 2d array
        # State consists of two variables: current day and current job index
        # Value is min job schedule found so far
        m = {}
        return self.dp(0, 0, m, jobDifficulty, d)

    # d -- day index
    # j -- job index to start from
    def dp(self, d: int, j: int, m: Dict, jobs: List[int], days: int) -> int:
        if (d, j) in m:
            return m[(d, j)]

        # Exit recursion when last day is reached
        if d == days - 1:
            max_day_job = max(jobs[j:])
            m[(d, j)] = max_day_job
            return max_day_job

        # General case
        # Iterate from j + 1 to len(jobs) - 1 - (days - d)
        # j + 1 -- if we take only one job for the current day
        # len(jobs) - 1 -- last job possible
        # (days - j) -- how many days are left to allocate
        min_total_schedule = float('inf')
        min_found = False
        r = len(jobs) - (days - d) + 2
        for ji in range(j + 1, r):
            # Find max day job if we take from j to ji
            max_day_job = max(jobs[j: ji])
            # calculate min job schedule for remaining days and jobs
            min_schedule = self.dp(d + 1, ji, m, jobs, days)

            if min_total_schedule > max_day_job + min_schedule:
                min_total_schedule = max_day_job + min_schedule
                min_found = True
        
        result = min_total_schedule if min_found else -1
        m[(d, j)] = result
        return result


s = Solution()
# jobs = [6, 5, 4, 3, 2, 1]
jobs = [9, 9, 9]
days = 4
res = s.minDifficulty(jobs, days)
print(res)
