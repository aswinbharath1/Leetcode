class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n & (n - 1 ) == 0 :
            x = log(n,4)
            return x.is_integer()
        return False