class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenth_pairs = {'{': '}', '(': ')', '[': ']'}
        
        for p in s:
            if p in parenth_pairs:
                stack.append(p)
                continue
            
            if not stack:
                return False
            
            last_open_p = stack.pop()
            if parenth_pairs[last_open_p] != p:
                return False
            
        return True if not stack else False
        