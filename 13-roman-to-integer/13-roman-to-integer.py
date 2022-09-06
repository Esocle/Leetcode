class Solution(object):
    def romanToInt(self, s):
        switcher = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        res = 0
        for i in range(len(s)-1):
            if switcher.get(s[i]) < switcher.get(s[i+1]):
                res -= switcher.get(s[i])
            else:
                res += switcher.get(s[i])

        res += switcher.get(s[-1])

        return res