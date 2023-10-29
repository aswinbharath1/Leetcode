class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        max_time = minutesToTest / minutesToDie + 1
        req_pigs = 0
        while (max_time) ** req_pigs < buckets:
            req_pigs += 1
        return req_pigs