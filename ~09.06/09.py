class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

a = Solution()
result = a.isPalindrome(-121)
print(result)