class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        result = 1
        while n > 4:
            result *= 3
            n -= 3

        return result * n
        