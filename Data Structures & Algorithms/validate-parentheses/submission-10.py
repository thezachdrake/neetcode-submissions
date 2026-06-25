class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        fronts: list[str] = ["(", "{", "["]
        for c in s:
            print(stack)
            if c in fronts:
                stack.append(c)
            if len(stack) == 0:
                return False
            match c:
                case ")":
                    if stack[-1] != "(":
                        return False
                    stack.pop()
                case "}":
                    if stack[-1] != "{":
                        return False
                    stack.pop()
                case "]":
                    if stack[-1] != "[":
                        return False
                    stack.pop()
        if len(stack) == 0:
            return True
        return False