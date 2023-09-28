class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e_num = []
        o_num = []
        for num in nums:
            if num % 2 == 0:
                e_num.append(num) 
            else:
                o_num.append(num)
        result = e_num + o_num
        
        return result