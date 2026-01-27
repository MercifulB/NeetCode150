class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closToOpen:
                if stack and stack[-1] == closToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
