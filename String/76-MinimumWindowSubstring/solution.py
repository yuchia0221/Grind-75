import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing_counter = len(t)
        window_start = window_end = current = 0
        memo = collections.Counter(t)

        for index, token in enumerate(s, 1):
            # Expand to find a valid window
            if memo[token] > 0:
                missing_counter -= 1
            memo[token] -= 1

            # Find a valid window
            if missing_counter == 0:
                # Contract to find a smaller and valid window
                while current < index and memo[s[current]] < 0:
                    memo[s[current]] += 1
                    current += 1

                if window_end == 0 or index-current < window_end-window_start:
                    window_start, window_end = current, index

                # Move forward to find a new window
                memo[s[current]] += 1
                missing_counter += 1
                current += 1

        return s[window_start:window_end]
