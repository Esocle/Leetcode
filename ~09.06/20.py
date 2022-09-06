class Solution(object):
    def isValid(self, s):
        branckets = {')':'(', '}':'{', ']':'['}
        stack = []
        for e in s:
            if branckets.get(e) != None:
                if len(stack) != 0:
                    temp = stack.pop()
                    if temp != branckets.get(e):
                        return False
                else:
                    return False
            else:
                stack.append(e)          
        if len(stack) == 0:
            return True
        else:
            return False


a = Solution()
result = a.isValid("{}}")
print(result)