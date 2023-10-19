class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(input_str):
            stack = []
            for char in input_str:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return process_string(s) == process_string(t)
