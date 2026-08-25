class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to track opening bracket 
        # if closing bracket ..check with top of the stack 
        # if its not matching then the string is invalid 
        stack = []
        dict_brackets = {')':'(','}':'{',']':'['}
        for char in s : 
            if char in dict_brackets:
                # if stack not empty and check open bracket == closing
                if stack and stack[-1] == dict_brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        # checking if stack is empty 
        return  not stack 

        # Time = o(n)
        # space = o(n)