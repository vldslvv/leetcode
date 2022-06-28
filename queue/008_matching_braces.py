
from collections import deque
class Solution:
    def is_opening_brace(self, c: str) -> bool:
        return c == '(' or c == '[' or c == '{'
    
    def is_matching(self, open: str, close: str):
        match close:
            case ')':
                return open == '('
            case ']':
                return open == '['
            case '}':
                return open == '{'
            case _:
                return False

        
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for c in s:
            if self.is_opening_brace(c):
                stack.append(c)
                continue
            
            # Only closing braces can be here since the task condition says so
            # If stack is empty and a closing brace appears
            if len(stack) == 0:
                return False

            top_char = stack.pop()
            if not self.is_matching(top_char, c):
                return False
            
        return len(stack) == 0