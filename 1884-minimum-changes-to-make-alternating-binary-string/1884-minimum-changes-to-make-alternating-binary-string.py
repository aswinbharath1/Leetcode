class Solution:
    def minOperations(self, s: str) -> int:
        res_start_one, res_start_zero = "", ""

        start_one, start_zero = 1, 0

        for i in range(len(s)):
            res_start_one += str(start_one)
            res_start_zero += str(start_zero)

            if start_one == 1:
                start_one = 0
            else:
                start_one = 1
            
            if start_zero == 0:
                start_zero = 1
            else:
                start_zero = 0
        
        count_zero, count_one = 0, 0

        for i in range(len(s)):
            if res_start_one[i] != s[i]:
                count_one += 1
            if res_start_zero[i] != s[i]:
                count_zero += 1

        return min(count_one, count_zero)