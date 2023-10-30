class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re 
        integers = [ int(i) for i in re.findall(r'\d+',word)]
        integers = set( integers)
        return len(integers)