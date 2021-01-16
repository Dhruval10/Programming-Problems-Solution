class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        # Check if length of string is 1. If that's the case then brackets won't be closed. So, we'll return False
        if length < 2:
            return False
        # If length > 1
        else:
            for i in range(length):
                # If s[i] is an opening bracket, then append it into a stack
                if s[i] != ')' and s[i] != ']' and s[i] != '}':
                    stack.append(s[i])
                # If the length of stack is 0 and s[i] is closing bracket, then return False
                elif len(stack) == 0 and (s[i] == ')' or s[i] == ']' or s[i] == '}'):
                    return False                
                # If popped and s[i] matches, then do nothing. But if they don't match then return false
                else:
                    popped = stack.pop()

                    if s[i] == ')' and popped == '(':
                        pass
                    elif s[i] == '}' and popped == '{':
                        pass
                    elif s[i] == ']' and popped == '[':
                        pass
                    else:
                        return False
            # if the braces opened and closed correctly, then stack will be empty at the end
            return True if len(stack) == 0 else False