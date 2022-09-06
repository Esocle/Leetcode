class Solution(object):
    def isValid(self, s):
        branckets = {')':'(', '}':'{', ']':'['}
        stack = []
        for e in s:
            if e in branckets:
                if stack:
                    top_element = stack.pop()
                    if top_element != branckets[e]:
                        return False
                else:
                    return False
            else:
                stack.append(e)
        
        return True if len(stack) == 0 else False
        