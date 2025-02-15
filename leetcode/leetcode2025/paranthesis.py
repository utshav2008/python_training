class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # Matching pairs
    
        for char in s:
            if char in mapping:
                # Pop top element if stack is not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  # Push opening bracket
                
        return not stack  # Stack should be empty if valid
